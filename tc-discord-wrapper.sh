#! /bin/bash
cd /home/larbs/LLM/TinyChatEngine/llm # CHANGE TO YOUR CHAT ENGINE PATH
#chatgpt
while true
do
	socat TCP-LISTEN:4000,reuseaddr EXEC:"./chat"
	sleep 1
done

