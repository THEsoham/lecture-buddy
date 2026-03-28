const loadingMessages = {
  process: ["🚀 Launching...", "📡 Fetching transcript...", "🧠 Storing in memory...", "✨ Almost there!"],
  summary: ["🤔 Reading the lecture...", "✍️ Writing summary...", "🌟 Polishing it up!"],
  quiz:    ["🎯 Finding key concepts...", "📝 Crafting questions...", "🧩 Almost ready!"],
  ask:     ["🔍 Searching the lecture...", "💡 Thinking hard...", "🎓 Got it!"]
}

let msgInterval = null

function startLoadingMessages(type, elementId) {
  const el = document.getElementById(elementId)
  let i = 0
  el.textContent = loadingMessages[type][0]
  msgInterval = setInterval(() => {
    i = (i + 1) % loadingMessages[type].length
    el.textContent = loadingMessages[type][i]
  }, 1200)
}

function stopLoadingMessages() {
  if (msgInterval) { clearInterval(msgInterval); msgInterval = null }
}

function switchTab(tabName, btn) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.add('hidden'))
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'))
  document.getElementById(tabName).classList.remove('hidden')
  btn.classList.add('active')
}

async function processVideo() {
  const videoId = document.getElementById('videoId').value.trim()
  const msg = document.getElementById('processMsg')
  const btn = document.getElementById('processBtn')
  const btnText = document.getElementById('processBtnText')

  if (!videoId) { msg.textContent = '⚠️ Please enter a video ID first!'; return }

  btn.disabled = true
  startLoadingMessages('process', 'processBtnText')
  msg.textContent = ''

  const res = await fetch('/process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ video_id: videoId })
  })
  const data = await res.json()

  stopLoadingMessages()
  btn.disabled = false
  btnText.textContent = '🚀 Let\'s Go!'
  msg.textContent = data.message || '❌ ' + data.error
}

async function getSummary() {
  const box = document.getElementById('summaryOutput')
  const btnText = document.getElementById('summaryBtnText')
  const btn = btnText.closest('button')

  btn.disabled = true
  box.innerHTML = '<span class="placeholder loading">✨ Generating summary...</span>'
  startLoadingMessages('summary', 'summaryBtnText')

  const res = await fetch('/summary')
  const data = await res.json()

  stopLoadingMessages()
  btn.disabled = false
  btnText.textContent = '✨ Generate Summary'
  box.textContent = data.summary || '❌ ' + data.error
}

async function getQuestions() {
  const box = document.getElementById('quizOutput')
  const btnText = document.getElementById('quizBtnText')
  const btn = btnText.closest('button')

  btn.disabled = true
  box.innerHTML = '<span class="placeholder loading">🎯 Generating quiz...</span>'
  startLoadingMessages('quiz', 'quizBtnText')

  const res = await fetch('/questions')
  const data = await res.json()

  stopLoadingMessages()
  btn.disabled = false
  btnText.textContent = '🎯 Generate Quiz'
  box.textContent = data.questions || '❌ ' + data.error
}

async function askQuestion() {
  const question = document.getElementById('question').value.trim()
  const box = document.getElementById('doubtOutput')
  const btnText = document.getElementById('askBtnText')
  const btn = btnText.closest('button')

  if (!question) { box.textContent = '⚠️ Type a question first!'; return }

  btn.disabled = true
  box.innerHTML = '<span class="placeholder loading">💡 Thinking...</span>'
  startLoadingMessages('ask', 'askBtnText')

  const res = await fetch('/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question })
  })
  const data = await res.json()

  stopLoadingMessages()
  btn.disabled = false
  btnText.textContent = '💡 Ask!'
  box.textContent = data.answer || '❌ ' + data.error
}