---
id: TC-GS-GSET-E2E-033-record-belum-ada-seed-default-dan-upsert-save-pertama
title: "Lifecycle: record General Settings belum ada — form terisi seed default dan Save pertama membuat record (upsert)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-117
coverage:
  web: automated
---

# Lifecycle: record General Settings belum ada — form terisi seed default dan Save pertama membuat record (upsert)

## Prerequisites

- Entitas `Client Tanpa Record` dengan record General Settings dihapus lewat database (failure injection oleh tim backend)
- Login sebagai Role: Total Control (staff `Client Tanpa Record`)

## Test Steps

1. Buka Global Settings > General Settings
2. Amati form
3. Verifikasi form terisi seed default tanpa error server: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`; Button "Save" disabled
4. Pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
5. Verifikasi save membuat record: toast sukses "Success, general settings has been saved."
6. Refresh halaman (F5)
7. Verifikasi Session Idle Timeout `1 hour` dan field lain tetap nilai seed default
8. Buka Modal Changelog
9. Verifikasi 1 baris Field `Session Idle Timeout`: Old Value `30 minutes` (nilai seed default), New Value `1 hour`

## Notes

- TC-GS-GSET-117 (Manual Only pada TC; failure injection di sisi backend). Save pertama bersifat upsert (LLD-DEV-008).
