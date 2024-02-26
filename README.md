# what-you-thought-first
年初に考えた目標を忘れないように LINE に通知します。
Cloud Functions にデプロイして、Cloud Scheduler からの POST リクエストを契機に LINE 通知を実施します。
Cloud Build からこのリポジトリを設定すると cloudbuild.yaml により CI/CD が行われます。

# 直接デプロイ
gcloud functions deploy send_thought`
 --runtime python39`
 --trigger-http`
 --allow-unauthenticated`
 --env-vars-file .env.yaml
