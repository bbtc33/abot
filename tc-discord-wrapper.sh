#! /bin/bash
cd /home/larbs/LLM/TinyChatEngine/llm
#chatgpt
while true
do
	socat TCP-LISTEN:4000,reuseaddr EXEC:"./chat"
	sleep 1
done

