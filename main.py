import os
import discord
from discord.ext import commands
from openai import OpenAI
import json
from dotenv import load_dotenv
import csv
import time

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

SYSTEM_PROMPT = """
Role: You are a Senior Linguistic Consultant specializing in Pragmatics and Digital Communication.
Objective: Analyze the provided Discord message for "Pragmatic Failure"—where the sender's intent may be misinterpreted due to a lack of social cues or poor framing.
Linguistic Constraints:
Grice’s Maxims: Evaluate if the message violates the Maxim of Manner (is it ambiguous or overly blunt?) or Quantity (is it too brief to be polite?).
Politeness Theory: Identify "Face-Threatening Acts." Use "hedging" (e.g., "I was wondering if..." or "It seems like...") to soften directives without losing clarity.
Output Format (JSON): 
{ "vibe_score": [0-100 score where 100 is perfectly prosocial and 0 is aggressive], 
"primary_tone": "[Brief description, e.g., 'Blunt/Directive']", 
"analysis": "[One sentence explaining the linguistic friction]", 
"rewrites": { "softened": "[A version using positive politeness and hedging]", 
"professional": "[A version optimized for clarity and workplace etiquette]", 
"direct": "[A version that is concise but removes aggressive undertones]" } }
"""

@bot.event
async def on_ready():
    print(f'{bot.user} is now online and analyzing pragmatics!')

@bot.command(name='check')
async def check_tone(ctx, *, message: str):
    await ctx.send("🔍 Analyzing linguistic pragmatics...")

    try:

        # Start the timer for latency tracking
        start_time = time.time()

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            response_format={ "type": "json_object" }
        )

        data = json.loads(response.choices[0].message.content)

        # Calculate latency
        latency = round(time.time() - start_time, 2)

        # Log the data to a CSV file
        with open('bot_analytics.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            # Log: Timestamp, Latency, Vibe Score, Primary Tone
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), latency, data['vibe_score'], data['primary_tone']])


        # Create a Discord Embed based on the vibe score
        color = discord.Color.green() if data['vibe_score'] > 70 else discord.Color.orange()
        if data['vibe_score'] < 40: color = discord.Color.red()

        embed = discord.Embed(title="Tone Analysis Results", color=color)
        embed.add_field(name="Vibe Score", value=f"{data['vibe_score']}/100", inline=True)
        embed.add_field(name="Primary Tone", value=data['primary_tone'], inline=True)
        embed.add_field(name="Linguistic Analysis", value=data['analysis'], inline=False)
        
        embed.add_field(name="💡 Softened", value=data['rewrites']['softened'], inline=False)
        embed.add_field(name="💼 Professional", value=data['rewrites']['professional'], inline=False)
        embed.add_field(name="🎯 Direct", value=data['rewrites']['direct'], inline=False)

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


bot.run(DISCORD_TOKEN)