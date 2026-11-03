---
id: TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups
title: "Group Context Header: Judul, Metrik Total Asset/Total User Exact-Match, dan Klik Angka Membuka Detail Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-24
  - TC-FA-GRP-26
  - TC-FA-GRP-27
  - TC-FA-GRP-28
  - TC-FA-GRP-968
coverage:
  web: automated
---

# Group Context Header: Judul, Metrik Total Asset/Total User Exact-Match, dan Klik Angka Membuka Detail Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Head Office (Function None, 0 aset langsung) > Floor 2 > IT Department (Code `ITD`, Assignable, 5 aset aktif). Total User Head Office dan IT Department dibaca lewat fixture BE.
- Kemampuan teknis: fixture BE (pembacaan Total Asset dan Total User exact-match per node) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-968: Group Context Header, satu judul dan metrik berlabel

1. Klik toggle expand-all pada sidebar
2. Klik IT Department di sidebar
3. Verifikasi Group Context Header memuat satu judul `IT Department` (nama polos tanpa path, badge Function, atau Code; tidak ada judul ganda)
4. Verifikasi header memuat dua metrik berlabel `Total Asset: 5` dan `Total User: [N]`
5. Verifikasi header berada di dalam Table SectionCard, di atas Toolbar

### TC-FA-GRP-24: Metrik header exact-match, sama dengan angka baris di All Groups

6. Klik node `All Groups` di sidebar
7. Catat angka Total Asset dan Total User pada baris Head Office
8. Klik Head Office di sidebar
9. Verifikasi header menampilkan satu judul `Head Office` dengan `Total Asset: 0` (exact-match, bukan 5)
10. Verifikasi header menampilkan `Total User: [N]` exact-match sesuai pembacaan fixture BE
11. Verifikasi angka header identik dengan angka baris Head Office di All Groups yang dicatat pada langkah 7

### TC-FA-GRP-26: Klik angka Total Asset lebih dari 0 pada header

12. Klik IT Department di sidebar
13. Klik angka Total Asset pada Group Context Header
14. Verifikasi Popup Detail Group terbuka pada tab Assets untuk Head Office > Floor 2 > IT Department
15. Verifikasi tab Assets berisi 5 aset
16. Tutup popup dengan [X]
17. Klik Floor 2 di sidebar
18. Klik angka Total Asset pada baris IT Department di tabel
19. Verifikasi tab Assets berisi 5 aset yang sama dengan langkah 15
20. Tutup popup dengan [X]

### TC-FA-GRP-27: Klik angka Total Asset 0 pada header

21. Klik Head Office di sidebar
22. Klik angka Total Asset `0` pada header
23. Verifikasi Popup Detail Group terbuka pada tab Assets (0 aset)
24. Verifikasi area tabel menampilkan Illustration dengan title `No assets assigned` dan body `No assets are currently assigned to this group.`
25. Tutup popup dengan [X]
26. Klik node `All Groups` di sidebar
27. Klik angka `0` pada baris Head Office di tabel
28. Verifikasi Popup Detail Group terbuka pada tab Assets dengan empty state yang sama seperti langkah 24
29. Tutup popup dengan [X]

### TC-FA-GRP-28: Klik angka Total User pada header

30. Klik Head Office di sidebar
31. Klik angka Total User pada header
32. Verifikasi Popup Detail Group terbuka pada tab Users untuk Head Office
33. Verifikasi jumlah baris tab Users sama dengan angka Total User header
34. Tutup popup dengan [X]

## Notes

- Spec 34 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 1 (expand-all), langkah 6 dan 26 (kembali ke `All Groups`), langkah 7 (mencatat angka sebagai baseline), langkah 16, 20, 25, 29, 34 (menutup popup), langkah 17 (memilih Floor 2 agar baris IT Department tampil untuk klik angka di kolom tabel).
- Urutan TC dalam spec: 968, 24, 26, 27, 28.
- Temuan untuk QA:
  - TC-FA-GRP-24 tidak menyebut nilai Total User Head Office; spec membandingkan header dengan baris All Groups dan pembacaan fixture BE.
  - TC-FA-GRP-26 butir b ("isi tab sama dengan klik angka di kolom tabel") tidak menyebut dimensi perbandingan; spec membandingkan jumlah aset (5).
