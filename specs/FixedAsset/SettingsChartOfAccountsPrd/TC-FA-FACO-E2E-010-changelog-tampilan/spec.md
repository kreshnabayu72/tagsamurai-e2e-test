---
id: TC-FA-FACO-E2E-010-changelog-tampilan
title: "Modal Changelog: Chart of Accounts menampilkan entri per field yang berubah"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r4", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§5#b8", "§8#r1", "§8.1#p1", "§8.1#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1#r4": 18
  "§4.1.1#r21": 25
  "§4.1.1#r22": [22, 27, 35]
  "§4.1.1#r23": [22, 29]
  "§4.1.1#r24": [22, 27, 28, 30, 35]
  "§4.1.1#r25": [23, 27, 28, 35]
  "§4.1.1#r26": [24, 27, 28, 36]
  "§4.1.1#r27": [26, 37]
  "§5#b8": 18
  "§8#r1": 18
  "§8.1#p1": [19, 21, 27, 28, 30, 34]
  "§8.1#p2": 31
coverage:
  web: automated
---

# Modal Changelog: Chart of Accounts menampilkan entri per field yang berubah

## Prerequisites
- Aktor: pengguna Total Control (nama lengkap terdiri dari nama depan dan nama belakang).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-010-1: akun `CL1-{runId}`, dibuat lewat form pada langkah spec ini dengan Account Name `Entri Awal {runId}`, Account Function `Asset Cost`, Status `Active`. Sesudah Edit: Account Name `Entri Ubah {runId}` dan Account Function `Gain on Disposal`, disimpan dalam satu Save. Sesudah itu akun dinonaktifkan lewat switch Status. Seluruh riwayat akun ini dihasilkan langkah spec ini, sehingga Changelog untuk Search `CL1-{runId}` berisi persis empat baris: Create, dua baris Edit, dan satu baris Status.
  - DU-010-2: akun `CL2-{runId}`, Account Name `Entri Hapus {runId}`, Account Function `Asset Cost`, Status `Active`, belum pernah punya entri Changelog. Akun ini dihapus pada langkah spec ini.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps
### Riwayat akun tampil di modal Changelog dengan kolom dan entri Create
1. Klik `[+ Account]`
2. Isi Account Code `CL1-{runId}`
3. Isi Account Name `Entri Awal {runId}`
4. Pilih `Asset Cost` pada field Account Function
5. Klik `[Submit]`
6. Ketik Search `CL1-{runId}`, tekan Enter
7. Klik `⋯` pada baris `CL1-{runId}` > `Edit`
8. Ganti isi Account Name dengan `Entri Ubah {runId}`
9. Pilih `Gain on Disposal` pada field Account Function
10. Klik `[Save]`
11. Klik switch Status baris `CL1-{runId}`
12. Klik `[Deactivate]` pada dialog `Deactivate Account`
13. Klik `(←)` pada kotak Search
14. Ketik Search `CL2-{runId}`, tekan Enter
15. Klik `⋯` pada baris `CL2-{runId}` > `Delete`
16. Klik `[Delete]` pada dialog `Delete Account`
17. Klik ikon Changelog
18. Verifikasi modal Changelog tampil dengan judul `Changelog: Chart of Accounts`
19. Verifikasi kolom modal berurutan Date, Action, Account Code, Field, Old Value, New Value, dan Modified By
20. Ketik Search `CL1-{runId}` pada modal Changelog, tekan Enter
21. Verifikasi modal memuat empat baris untuk Account Code `CL1-{runId}`
22. Verifikasi baris Create tampil dengan Action `Create`, Account Code `CL1-{runId}`, dan Field `Account Code`
23. Verifikasi Old Value baris Create bernilai `—`
24. Verifikasi New Value baris Create bernilai `CL1-{runId}`
25. Verifikasi Date baris Create terisi tanggal dengan Date Format `dd/MM/yy`
26. Verifikasi Modified By baris Create menampilkan nama depan aktor diikuti inisial nama belakangnya, format `[First Name] [Last Initial]`

### Edit dua field dalam satu Save menulis satu baris per field
27. Verifikasi baris dengan Action `Edit` dan Field `Account Name` bernilai Old Value `Entri Awal {runId}` dan New Value `Entri Ubah {runId}`
28. Verifikasi baris dengan Action `Edit` dan Field `Account Function` bernilai Old Value `Asset Cost` dan New Value `Gain on Disposal`
29. Verifikasi Account Code kedua baris Edit bernilai `CL1-{runId}`

### Deactivate menulis satu baris Status dengan nilai polos
30. Verifikasi baris dengan Action `Edit` dan Field `Status` bernilai Old Value `Active` dan New Value `Inactive`
31. Verifikasi Old Value dan New Value baris Status tampil sebagai teks polos, bukan badge atau switch

### Delete menulis satu baris dengan New Value kosong
32. Klik `(←)` pada kotak Search modal Changelog
33. Ketik Search `CL2-{runId}` pada modal Changelog, tekan Enter
34. Verifikasi modal memuat satu baris untuk Account Code `CL2-{runId}`
35. Verifikasi baris tampil dengan Action `Delete`, Field `Account Code`, dan Old Value `CL2-{runId}`
36. Verifikasi New Value baris Delete bernilai `—`
37. Verifikasi Modified By baris Delete menampilkan format `[First Name] [Last Initial]`
