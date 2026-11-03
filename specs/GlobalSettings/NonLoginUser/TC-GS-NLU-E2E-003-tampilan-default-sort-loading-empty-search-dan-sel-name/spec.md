---
id: TC-GS-NLU-E2E-003-tampilan-default-sort-loading-empty-search-dan-sel-name
title: "Tampilan default sort, loading, empty Search, dan sel Name, Position, Employee ID, Represented By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-7
  - TC-GS-NLU-8
  - TC-GS-NLU-10
  - TC-GS-NLU-12
  - TC-GS-NLU-13
  - TC-GS-NLU-14
  - TC-GS-NLU-15
coverage:
  web: automated
---

# Tampilan default sort, loading, empty Search, dan sel Name, Position, Employee ID, Represented By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza, Default User entitas), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk akun aktor sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: Non-Login User Budi Kurniawan (foto, Position Field Technician, Represented By Ahmad Fauzi) dan Siti Rahayu (tanpa foto, tanpa Position dan Employee ID, Division Warehouse) (No. 11), serta Login User Ahmad Fauzi (No. 10), hanya dibaca. Pre-setup berisi lebih dari 10 Non-Login User sehingga halaman pertama penuh.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons list Non-Login User saja (bukan kegagalan; menahan respons hanya untuk mengamati state Loading) di atas backend nyata. Intercept dilepas pada langkah 6.
- Spec hanya membaca; Search yang dipakai dipulihkan lewat langkah penghubung. Tidak ada state global yang diubah.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-7: Default sort tabel Non-Login User Name A-Z saat pertama dibuka

1. Verifikasi sepuluh baris pertama terurut Name A-Z case-insensitive tanpa baris yang melanggar urutan alfabet
2. Verifikasi tidak ada indikator sort aktif pada header kolom selain default Name

### TC-GS-NLU-8: Loading state tabel Non-Login User menampilkan indikator loading

3. Tahan respons list Non-Login User (intercept), lalu muat ulang halaman (F5) pada sub-tab Non-Login User
4. Verifikasi Loading component `S-01` tampil di area tabel
5. Verifikasi empty state dan error state tidak tampil
6. Lepas tahanan respons list Non-Login User
7. Verifikasi indikator loading diganti baris data

### TC-GS-NLU-10: Empty state hasil pencarian tidak ditemukan pada tabel Non-Login User

8. Klik icon Search, ketik Search `zzzxxx`, tekan Enter
9. Verifikasi empty state `S-06`: Illustration dengan Title `"No results found"` dan Description `"Try adjusting your search or filter."`
10. Klik `(←)` pada kotak Search

### TC-GS-NLU-12: Kolom Name menampilkan avatar foto atau placeholder dan hover identifier

11. Klik icon Search, ketik Search `Budi Kurniawan`, tekan Enter
12. Verifikasi sel Name baris Budi Kurniawan berbentuk `[Avatar] Full Name` dalam satu sel dengan thumbnail foto bulat
13. Hover teks Name Budi Kurniawan
14. Verifikasi warna teks Name berubah ke warna primary Global Settings
15. Verifikasi teks Name tanpa garis bawah
16. Ganti isi kotak search dengan `Siti Rahayu`, tekan Enter
17. Verifikasi sel Name baris Siti Rahayu berbentuk `[Avatar] Full Name` dalam satu sel dengan avatar placeholder generik

### TC-GS-NLU-14: Nilai kosong Position dan Employee ID tampil strip

18. Verifikasi sel Position baris Siti Rahayu menampilkan `—`
19. Verifikasi sel Employee ID baris Siti Rahayu menampilkan `—`
20. Verifikasi sel Division baris Siti Rahayu tidak kosong (`Warehouse`)

### TC-GS-NLU-15: Kolom Represented By tampil format singkat dengan tooltip nama penuh dan buka Detail Login User

21. Ganti isi kotak search dengan `Budi Kurniawan`, tekan Enter
22. Verifikasi sel Represented By baris Budi Kurniawan menampilkan `Ahmad F` sebagai text link
23. Hover teks Represented By `Ahmad F`
24. Verifikasi Tooltip hover `Ahmad Fauzi`
25. Klik teks Represented By `Ahmad F`
26. Verifikasi navigasi ke Detail Login User Ahmad Fauzi

### TC-GS-NLU-13: Klik Name membuka Detail di tab yang sama dan klik area baris lain tidak melakukan apa pun

27. Klik menu `User` di sidebar Global Settings, lalu klik sub-tab `Non-Login User` (Search ter-reset), ketik Search `Budi Kurniawan`, tekan Enter
28. Klik area sel Position pada baris Budi Kurniawan
29. Verifikasi tidak ada navigasi dari halaman List
30. Verifikasi tidak ada popup
31. Klik teks Name Budi Kurniawan
32. Verifikasi navigasi ke Detail Non-Login User Budi Kurniawan
33. Verifikasi Detail terbuka pada tab browser yang sama

## Notes

- Langkah penghubung (S-03, R-16): langkah 10, 11, 16, 21, 27 (Search untuk menemukan baris target, mengosongkan Search, dan membuka ulang List sesudah navigasi ke Detail).
- Penyimpangan urutan (S-10): TC-GS-NLU-14 diletakkan sesudah TC-GS-NLU-12 karena baris Siti Rahayu sudah tersaring oleh Search TC-GS-NLU-12. TC-GS-NLU-15 dan TC-GS-NLU-13 diletakkan di akhir karena kliknya meninggalkan List (navigasi ke Detail Login User dan Detail Non-Login User).
- Search baris target (Budi Kurniawan, Siti Rahayu) dicatat sebagai langkah penghubung karena Pre-setup berisi lebih dari 10 baris dan baris target belum tentu di halaman pertama.
- Temuan untuk QA:
  - TC-GS-NLU-12 langkah 1 meminta mengamati Budi Kurniawan dan Siti Rahayu bersamaan; baris keduanya tidak selalu berada pada satu halaman, sehingga spec mengamati keduanya bergantian lewat Search.
  - TC-GS-NLU-8 Expected a menyebut `S-01`, `S-02`, `S-06` (kode state PRD); spec menyalin kode itu apa adanya sebagai nama state.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
