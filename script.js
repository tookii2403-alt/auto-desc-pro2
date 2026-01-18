async function generateCopy() {
    const description = document.getElementById('description').value;
    const target = document.getElementById('target-audience').value; // 追加
    const resultDiv = document.getElementById('result');

    if (!description) {
        alert("商品の特徴を入力してください！");
        return;
    }

    resultDiv.innerText = "生成中...";

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description, target }), // ターゲットを追加して送信
        });

        const data = await response.json();
        if (data.copy) {
            resultDiv.innerText = data.copy;
        } else {
            resultDiv.innerText = "エラーが発生しました。";
        }
    } catch (e) {
        resultDiv.innerText = "通信エラーが発生しました。";
    }
}
