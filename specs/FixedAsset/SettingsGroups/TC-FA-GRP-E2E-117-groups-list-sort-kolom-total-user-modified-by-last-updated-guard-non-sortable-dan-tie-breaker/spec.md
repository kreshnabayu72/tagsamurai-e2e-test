---
id: TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker
title: "Groups List Sort Kolom Total User, Modified By, Last Updated, Guard Kolom Non-Sortable, dan Tie-Breaker Deterministik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-371
  - TC-FA-GRP-372
  - TC-FA-GRP-373
  - TC-FA-GRP-374
  - TC-FA-GRP-1132
coverage:
  web: automated
---

# Groups List Sort Kolom Total User, Modified By, Last Updated, Guard Kolom Non-Sortable, dan Tie-Breaker Deterministik

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-117`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-117` | `V117L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-117` | `V117K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-117` | `V117J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-117` | `V117I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-117` | `V117H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-117` | `V117G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-117` | `V117F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-117` | `V117E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-117` | `V117D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-117` | `V117C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-117` | `V117B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-117` | `V117A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-117`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-371, 372, 373 (kolom Total User, Modified By, Last Updated), urutan baris = urutan iterasi. Tabel dibatasi Search suffix spec (12 baris; 10 baris di halaman 1). `ModFirst` = nama lengkap Modified By yang lebih awal secara alfabet di antara `ModA` dan `ModB`; `ModLast` = yang lebih akhir (nama lengkap keduanya dibaca sebelum uji). Batch 1 = `Alpha {runId}-117`, `bravo {runId}-117`, `Charlie {runId}-117`, `delta {runId}-117`, `Echo {runId}-117`, `foxtrot {runId}-117`, `Golf {runId}-117`; batch 2 = `hotel {runId}-117`, `India {runId}-117`, `juliet {runId}-117`, `Kilo {runId}-117`, `lima {runId}-117`. Total User terurut: 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 12.

| Kolom | Setelah klik #1 (Ascending) | Setelah klik #2 (Descending) |
|---|---|---|
| Total User | baris 1 bernilai 3 dan baris 10 = `Golf {runId}-117` (6) | baris 1 sampai 3 = `Echo {runId}-117`, `juliet {runId}-117`, `Golf {runId}-117` |
| Modified By | baris 1 ber-Modified By `ModFirst` | baris 1 ber-Modified By `ModLast` |
| Last Updated | baris 1 adalah salah satu group batch 1 (Oldest First) | baris 1 adalah salah satu group batch 2 (Newest First) |
- Data Dinamis TC-FA-GRP-1132 (suffix spec): group `Tie Parent {runId}-117` (level 1, Function None) dengan 12 child Assignable ber-Total Asset 0: `Tie 01 {runId}-117` sampai `Tie 12 {runId}-117`, dibuat lewat API di `before` dan dihapus di `after`. Page size 10: halaman 1 = Tie 01 sampai Tie 10, halaman 2 = Tie 11 dan Tie 12. Dipakai sebagai pengganti Head Office >= 12 child pada TC (S-06).

## Test Steps

1. Ketik Search `{runId}-117`, tekan Enter

### TC-FA-GRP-371, 372, 373: Sort per kolom Total User, Modified By, dan Last Updated (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 9): jalankan langkah berikut dengan kolom pada baris itu
3. Verifikasi header kolom pada baris tabel tampil di tabel
4. Klik header kolom pada baris tabel satu kali
5. Verifikasi urutan tabel sesuai sel "Setelah klik #1 (Ascending)" baris tabel
6. Klik header kolom yang sama satu kali lagi
7. Verifikasi urutan tabel sesuai sel "Setelah klik #2 (Descending)" baris tabel
8. Klik header kolom yang sama satu kali lagi
9. Verifikasi urutan tabel kembali ke default: baris 1 sampai 3 = `Alpha {runId}-117`, `bravo {runId}-117`, `Charlie {runId}-117` (Group A-Z)
10. Klik `(←)` pada kotak Search

### TC-FA-GRP-374: Guard kolom non-sortable Checkbox dan Column Visibility (⋯)

11. Catat urutan baris halaman 1 tabel
12. Verifikasi header kolom Checkbox tidak punya ikon sort
13. Verifikasi header kolom Column Visibility (`⋯`) tidak punya ikon sort
14. Klik checkbox pada header kolom Checkbox
15. Verifikasi urutan baris halaman 1 tidak berubah dari yang dicatat
16. Klik checkbox pada header kolom Checkbox untuk membatalkan seleksi
17. Klik icon `⋯` pada header kolom Column Visibility
18. Verifikasi urutan baris halaman 1 tidak berubah dari yang dicatat
19. Tekan Esc untuk menutup overlay Column Visibility

### TC-FA-GRP-1132: Tie-breaker deterministik antar halaman

20. Klik `Tie Parent {runId}-117` di sidebar Group Tree
21. Klik header Function satu kali (Ascending)
22. Verifikasi halaman 1 berurutan Group A-Z: `Tie 01 {runId}-117` sampai `Tie 10 {runId}-117`
23. Pindah ke halaman 2 lewat pagination
24. Verifikasi halaman 2 berurutan: `Tie 11 {runId}-117`, lalu `Tie 12 {runId}-117`
25. Klik header Total Asset satu kali (Ascending)
26. Pindah ke halaman 1 lewat pagination
27. Verifikasi halaman 1 berurutan Group A-Z: `Tie 01 {runId}-117` sampai `Tie 10 {runId}-117`
28. Pindah ke halaman 2 lewat pagination
29. Verifikasi halaman 2 berurutan: `Tie 11 {runId}-117`, lalu `Tie 12 {runId}-117`
30. Muat ulang halaman (F5)
31. Klik `Tie Parent {runId}-117` di sidebar Group Tree
32. Klik header Function satu kali (Ascending)
33. Verifikasi halaman 1 berurutan Group A-Z: `Tie 01 {runId}-117` sampai `Tie 10 {runId}-117` (urutan tidak berubah antar pemuatan ulang)

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 9 diulang untuk tiap baris tabel parameter iterasi (Total User, Modified By, Last Updated): 3 iterasi x 7 langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec dan menutupnya, mencatat urutan baris, membatalkan seleksi header, menutup overlay dengan Esc, membuka node `Tie Parent` di sidebar, dan berpindah halaman (S-03, S-09, R-16).
- Urutan TC dipertahankan: TC-FA-GRP-1132 di akhir karena berpindah ke node `Tie Parent` dan memuat ulang halaman.
- Klik #2 TC-FA-GRP-372 (Modified By) diasersi pada nama lengkap, bukan singkatan tampilan (R-14); nama lengkap `ModA` dan `ModB` dibaca sebelum uji.
- Spec 33 langkah (ekspansi iterasi ± 40 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-374 Expected "tidak mengubah urutan saat diklik" untuk header Checkbox: mengklik header Checkbox memilih semua baris; spec mengklik lalu membatalkan seleksi dan hanya mengasersi urutan.
  - TC-FA-GRP-1132 memakai Head Office >= 12 child (Pre-setup); spec memakai `Tie Parent` milik spec agar Pre-setup tidak diubah (S-06).
