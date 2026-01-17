async function generateCopy() {
    const description = document.getElementById('product-description').value;
    const result = document.getElementById('copy-result');
    const spinner = document.getElementById('loading-spinner');
    
    if (!description) {
        alert("商品名や特徴を入力してください");
        return;
    }

    // 読み込み中を表示
    spinner.style.display = 'block';
    result.textContent = 'AIコピーライターが生成中...';

    try {
        // AIの頭脳（app.py）にリクエストを送る
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ description: description })
        });

        const data = await response.json();
        
        if (data.copy) {
            result.textContent = data.copy;
        } else {
            result.textContent = "エラーが発生しました";
        }
    } catch (e) {
        result.textContent = "サーバーに接続できませんでした";
    } finally {
        spinner.style.display = 'none';
    }
}
