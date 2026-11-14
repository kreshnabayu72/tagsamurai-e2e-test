---
id: TC-FA-FACO-E2E-011-changelog-entri-edit
title: "Edit beruntun menulis entri Changelog per field tanpa mengubah entri lama"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§8.1#p3", "EB-LOG-1", "EB-LOG-2", "L-02"]
smoke: ["L-02"]
dependsOn: []
trace:
  "§8.1#p3": [10, 13, 25, 27]
  "EB-LOG-1": [9, 14, 16, 24]
  "EB-LOG-2": [25, 26]
  "L-02": [9, 10, 11, 12]
anchor: [9]
coverage:
  web: automated
---

# Edit beruntun menulis entri Changelog per field tanpa mengubah entri lama

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-011-1: akun `LG1-{runId}`, Account Name `Nama Satu {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0, Last Used in Journal kosong, belum pernah punya entri Changelog. Edit pertama mengubah tiga field dalam satu Save: Account Code `LG1B-{runId}`, Account Name `Nama Dua {runId}`, Account Function `Gain on Disposal`. Edit kedua hanya mengubah Account Name menjadi `Nama Tiga {runId}`.
  - DU-011-2: akun `LG2-{runId}`, Account Name `Akun Pembanding {runId}`, Account Function `Asset Cost`, Status `Active`, tidak diubah oleh spec ini dan belum pernah punya entri Changelog.

## Test Steps
### Edit tiga field sekaligus menulis satu entri per field dengan Account Code sesudah perubahan
1. Ketik Search `LG1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `LG1-{runId}` > `Edit`
3. Ganti isi Account Code dengan `LG1B-{runId}`
4. Ganti isi Account Name dengan `Nama Dua {runId}`
5. Pilih `Gain on Disposal` pada field Account Function
6. Klik `[Save]`
7. Klik ikon Changelog
8. Ketik Search `LG1B-{runId}` pada modal Changelog, tekan Enter
9. Verifikasi modal Changelog memuat tiga baris Action `Edit` untuk Account Code `LG1B-{runId}`, dengan Field `Account Code`, `Account Name`, dan `Account Function`
10. Verifikasi baris Field `Account Code` bernilai Old Value `LG1-{runId}` dan New Value `LG1B-{runId}`
11. Verifikasi baris Field `Account Name` bernilai Old Value `Nama Satu {runId}` dan New Value `Nama Dua {runId}`
12. Verifikasi baris Field `Account Function` bernilai Old Value `Asset Cost` dan New Value `Gain on Disposal`
13. Verifikasi kolom Account Code pada ketiga baris bernilai `LG1B-{runId}`, kode sesudah perubahan, bukan `LG1-{runId}`
14. Verifikasi tidak ada baris Field `Status` untuk Account Code `LG1B-{runId}` karena Status tidak berubah

### Edit tidak menulis entri di akun lain
15. Ganti isi kotak Search modal Changelog dengan `LG2-{runId}`, tekan Enter
16. Verifikasi `No results found` tampil di modal Changelog karena akun `LG2-{runId}` tidak diubah

### Edit beruntun tidak mengubah entri yang sudah ditulis
17. Tutup modal Changelog
18. Ganti isi kotak Search dengan `LG1B-{runId}`, tekan Enter
19. Klik `⋯` pada baris `LG1B-{runId}` > `Edit`
20. Ganti isi Account Name dengan `Nama Tiga {runId}`
21. Klik `[Save]`
22. Klik ikon Changelog
23. Ketik Search `LG1B-{runId}` pada modal Changelog, tekan Enter
24. Verifikasi modal Changelog memuat empat baris untuk Account Code `LG1B-{runId}`, yaitu tiga baris Edit pertama ditambah satu baris Edit kedua
25. Verifikasi entri rename pertama tetap menampilkan Old Value `Nama Satu {runId}` dan New Value `Nama Dua {runId}`
26. Verifikasi entri rename kedua menampilkan Old Value `Nama Dua {runId}` dan New Value `Nama Tiga {runId}`
27. Verifikasi baris Field `Account Code` tetap bernilai Old Value `LG1-{runId}` dan New Value `LG1B-{runId}`, tidak mengikuti kode terbaru
