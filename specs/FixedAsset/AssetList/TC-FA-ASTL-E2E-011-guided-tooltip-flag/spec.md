---
id: TC-FA-ASTL-E2E-011-guided-tooltip-flag
title: "Guided tooltip tidak muncul lagi sesudah selesai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-TBL-10]
smoke: []
dependsOn: []
trace:
  EB-TBL-10: [3, 7, 13, 15, 20, 24, 31, 35, 38]
anchor: [6, 12, 19, 30]
coverage:
  web: automated
---

# Guided tooltip tidak muncul lagi sesudah selesai

## Prerequisites
- Aktor: Total Control `Siti Rahma {runId}`, yang belum pernah membuka halaman Assets, serta Total Control `Joko Prasetyo {runId}` dan `Maya Kusuma {runId}` yang juga belum pernah membuka halaman Assets.
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-011-1: User `Siti Rahma {runId}`, role Total Control, cakupan seluruh client, belum pernah membuka halaman Assets.
  - DU-011-3: User `Joko Prasetyo {runId}`, role Total Control, cakupan seluruh client, belum pernah membuka halaman Assets.
  - DU-011-4: User `Maya Kusuma {runId}`, role Total Control, cakupan seluruh client, belum pernah membuka halaman Assets.
  - DU-011-2: Aset `Printer Laser - 1 {runId}`, berstatus `Available`.
- Kondisi:
  - Akun `Siti Rahma {runId}`, `Joko Prasetyo {runId}`, dan `Maya Kusuma {runId}` aktif dan kredensialnya tersedia.

## Test Steps

### Walkthrough muncul otomatis di kunjungan pertama dan tidak muncul lagi sesudah Skip
1. Masuk sebagai `Siti Rahma {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Verifikasi walkthrough Guided Tooltip tampil otomatis pada kunjungan pertama
4. Klik `[Skip]`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris `Printer Laser - 1 {runId}` tampil
7. Verifikasi walkthrough Guided Tooltip tidak tampil

### Flag bertahan antar sesi
8. Keluar dari akun
9. Masuk sebagai `Siti Rahma {runId}`
10. Klik menu `Fixed Asset > Assets` pada sidebar
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris `Printer Laser - 1 {runId}` tampil
13. Verifikasi walkthrough Guided Tooltip tidak tampil pada kunjungan berikutnya

### Replay memutar ulang tanpa mereset flag
14. Klik `[?]`
15. Verifikasi walkthrough Guided Tooltip tampil
16. Klik `[Skip]`
17. Muat ulang halaman
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi baris `Printer Laser - 1 {runId}` tampil
20. Verifikasi walkthrough Guided Tooltip tidak tampil sesudah replay dan muat ulang halaman

### Walkthrough yang diselesaikan lewat Done tidak muncul lagi
21. Keluar dari akun
22. Masuk sebagai `Joko Prasetyo {runId}`
23. Klik menu `Fixed Asset > Assets` pada sidebar
24. Verifikasi walkthrough Guided Tooltip tampil otomatis pada kunjungan pertama
25. Klik `[Next]`
26. Klik `[Next]`
27. Klik `[Done]`
28. Muat ulang halaman
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi baris `Printer Laser - 1 {runId}` tampil
31. Verifikasi walkthrough Guided Tooltip tidak tampil sesudah diselesaikan lewat `[Done]`

### Walkthrough yang ditinggalkan tanpa selesai muncul lagi di kunjungan berikutnya
32. Keluar dari akun
33. Masuk sebagai `Maya Kusuma {runId}`
34. Klik menu `Fixed Asset > Assets` pada sidebar
35. Verifikasi walkthrough Guided Tooltip tampil otomatis pada kunjungan pertama
36. Klik menu lain pada sidebar selain `Fixed Asset > Assets` tanpa menekan `[Skip]` atau `[Done]`
37. Klik menu `Fixed Asset > Assets` pada sidebar
38. Verifikasi walkthrough Guided Tooltip tampil lagi karena flag belum disetel
