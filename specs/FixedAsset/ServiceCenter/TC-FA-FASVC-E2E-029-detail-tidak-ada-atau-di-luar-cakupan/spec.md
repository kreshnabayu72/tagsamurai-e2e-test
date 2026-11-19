---
id: TC-FA-FASVC-E2E-029-detail-tidak-ada-atau-di-luar-cakupan
title: "URL Detail Tidak Ada atau di Luar Cakupan: Halaman Page Not Found"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#p5"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#p5": [2, 3, 4, 6, 7, 8, 16, 17, 18, 21, 22, 23]
anchor: []
coverage:
  web: automated
---

# URL Detail Tidak Ada atau di Luar Cakupan: Halaman Page Not Found

## Prerequisites
- Aktor: Total Control. Aktor lain: Group Manager `Dimas Prakoso {runId}`.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-029-1: ID Service Center `id-tidak-ada-{runId}`, tidak dimiliki Service Center mana pun.
  - DU-029-2: Service Center `Vendor Entitas Lain {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Sibu {runId}`, Company phone `+60 8555100101`, ada di entitas lain (bukan entitas aktor).
  - DU-029-3: Service Center `Detail Terhapus {runId}`, Status `Active`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Kluang {runId}`, Company phone `+60 7555100202`, Usage `0`.
  - DU-029-4: Group `Cabang Selatan {runId}` dan Group `Cabang Utara {runId}`, tidak saling induk.
  - DU-029-5: User `Dimas Prakoso {runId}`, Role `Group Manager`, cakupan Group `Cabang Selatan {runId}`.
  - DU-029-6: Service Center `Vendor Luar Cakupan {runId}`, Status `Active`, Service type `Routine`, Available to `Cabang Utara {runId}`, Country `Malaysia`, City `Alor Gajah {runId}`, Company phone `+60 6555100303`.
- Kondisi: akun `Dimas Prakoso {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### URL Detail dengan ID yang tidak ada
1. Buka URL Detail Service Center dengan ID `id-tidak-ada-{runId}`
2. Verifikasi halaman menampilkan judul `Page Not Found`
3. Verifikasi halaman menampilkan teks `The page you're looking for doesn't exist or may have been moved.`
4. Verifikasi halaman menampilkan tombol `Go to Dashboard`

### URL Detail Service Center milik entitas lain
5. Buka URL Detail Service Center `Vendor Entitas Lain {runId}`
6. Verifikasi halaman menampilkan judul `Page Not Found`
7. Verifikasi halaman menampilkan teks `The page you're looking for doesn't exist or may have been moved.`
8. Verifikasi halaman menampilkan tombol `Go to Dashboard`

### URL Detail Service Center yang sudah dihapus
9. Ketik Search `Detail Terhapus {runId}`, tekan Enter
10. Klik Name `Detail Terhapus {runId}`
11. Catat URL halaman Detail `Detail Terhapus {runId}`
12. Klik `⋯` pada header Detail
13. Klik `Delete`
14. Klik `[Delete]` pada dialog `Delete Service Center`
15. Buka URL Detail yang dicatat pada langkah 11
16. Verifikasi halaman menampilkan judul `Page Not Found`
17. Verifikasi halaman menampilkan teks `The page you're looking for doesn't exist or may have been moved.`
18. Verifikasi halaman menampilkan tombol `Go to Dashboard`

### URL Detail Service Center di luar cakupan Group aktor
19. Masuk sebagai `Dimas Prakoso {runId}`
20. Buka URL Detail Service Center `Vendor Luar Cakupan {runId}`
21. Verifikasi halaman menampilkan judul `Page Not Found`
22. Verifikasi halaman menampilkan teks `The page you're looking for doesn't exist or may have been moved.`
23. Verifikasi halaman menampilkan tombol `Go to Dashboard`
