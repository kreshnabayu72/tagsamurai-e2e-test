---
id: TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal
title: "Activate Trial: Screening dan Nilai Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-176
  - TC-AC-CS-181
  - TC-AC-CS-177
  - TC-AC-CS-180
  - TC-AC-CS-182
coverage:
  web: automated
---

# Activate Trial: Screening dan Nilai Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-046` (padanan Pre-setup #48: tanpa term dan tanpa trial). Tidak ada Submit pada spec ini.
- State global yang diubah (suite serial) dan pemulihannya di hook `after` lewat fixture BE (disediakan tim FE/BE): ceiling Trial awal `Max Trial Duration` 60 day(s), `Max Trial Asset Quota` 200 assets, `Max Trial Concurrent User Quota` 50 users (Pre-setup #25) diubah menjadi 20, 30, dan 5 pada langkah 30 untuk TC-AC-CS-182 lalu dipulihkan.

## Test Steps

### TC-AC-CS-176: Screening modal Activate Trial Product FAMS atau SAMS

1. Klik `[+ Activate Trial]`
2. Verifikasi header modal berjudul "Activate Trial" dengan tombol silang `[✕]`
3. Verifikasi Client * (Searchable dropdown, placeholder "Select client"), Product * (placeholder "Select product"), dan Plan * (placeholder "Select plan", helper "Plans this client has already trialed are not listed")
4. Verifikasi Trial Duration * (addon `day(s)`, placeholder "Enter trial duration", helper "Maximum 60 days")
5. Verifikasi Trial Asset Quota * (addon `assets`, placeholder "Enter asset quota", helper "Maximum 200 assets")
6. Verifikasi Trial Concurrent User Quota * (addon `users`, placeholder "Enter concurrent user quota", helper "Maximum 50 users")
7. Verifikasi Trial Log Source Quota tidak tampil
8. Verifikasi footer: checkbox "Stay on this form after submitting" rata kanan, lalu `[Clear Field]` dan `[Submit]` rata kanan

### TC-AC-CS-181: Nilai awal form Activate Trial (Product FAMS)

9. Pilih Product `FAMS`
10. Verifikasi nilai awal FAMS Trial Duration `30`
11. Verifikasi nilai awal FAMS Trial Asset Quota `50`
12. Verifikasi nilai awal FAMS Trial Concurrent User Quota `10`

### TC-AC-CS-177: Screening modal Activate Trial Product SIEM

13. Pilih Product `SIEM`
14. Verifikasi Trial Log Source Quota * tampil dengan addon `sources`, placeholder "Enter log source quota", helper "Between 1 and 9999 sources"
15. Verifikasi Trial Concurrent User Quota * tampil dengan helper "Maximum 50 users"
16. Verifikasi Trial Asset Quota tidak tampil
17. Verifikasi Trial Duration * tampil dengan helper "Maximum 60 days"

### TC-AC-CS-181: Nilai awal form Activate Trial (Product SIEM)

18. Verifikasi nilai awal SIEM Trial Duration `30`
19. Verifikasi nilai awal SIEM Trial Concurrent User Quota `10`
20. Verifikasi nilai awal SIEM Trial Log Source Quota `10`
21. Klik `[Clear Field]`

### TC-AC-CS-180: Dropdown Plan kosong sebelum Client dan Product dipilih

22. Buka dropdown Plan sebelum memilih Client dan Product
23. Verifikasi dropdown Plan terbuka (daftar opsi tampil sebagai surface dropdown)
24. Verifikasi dropdown Plan belum berisi opsi
25. Tekan `Esc` untuk menutup dropdown Plan
26. Pilih Client `Client Tanpa Subscription+{runId}-046` dan Product `FAMS`, lalu buka dropdown Plan
27. Verifikasi daftar plan Paid aktif Product `FAMS` terisi berurut menurut rank
28. Tekan `Esc` untuk menutup dropdown Plan
29. Klik `[Clear Field]`, lalu klik `[✕]` pada header modal

### TC-AC-CS-182: Ceiling lebih kecil dari default form menjadi nilai awal

30. Ubah ceiling Trial menjadi `Max Trial Duration` 20, `Max Trial Asset Quota` 30, dan `Max Trial Concurrent User Quota` 5 lewat fixture BE hingga tersimpan
31. Klik `[+ Activate Trial]`
32. Pilih Product `FAMS`
33. Verifikasi nilai awal Trial Duration `20`
34. Verifikasi nilai awal Trial Asset Quota `30`
35. Verifikasi nilai awal Trial Concurrent User Quota `5`
36. Isi Trial Duration `21`
37. Verifikasi error "Trial duration cannot exceed 20 days"
38. Klik `[✕]` pada header modal
39. Verifikasi dialog Unsaved Changes tampil
40. Klik `[Leave]`
41. Pulihkan ceiling Trial ke 60, 200, dan 50 lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular; TC-AC-CS-181 diamati dalam dua bagian (FAMS pada langkah 10 sampai 12, SIEM pada langkah 18 sampai 20) pada pembukaan form yang sama dengan TC-AC-CS-176 dan TC-AC-CS-177 (satu pembukaan form untuk kasus tanpa submit). TC-AC-CS-177 melanjutkan TC-AC-CS-176 menurut Dependensi TC. Urutan mengikuti screening lebih dulu (TC-AC-CS-176, 181, 177), baru TC-AC-CS-180 yang memilih Client dan Product, supaya placeholder diasersi sebelum terisi (S-14).
- Langkah penghubung (S-03): `Esc` menutup dropdown (langkah 25, 28), `[Clear Field]` pada langkah 21 (mengosongkan Product SIEM sebelum TC-AC-CS-180) dan `[Clear Field]` lalu `[✕]` pada langkah 29 (form kembali clean), pengaturan dan pemulihan ceiling lewat fixture BE (langkah 30, 41; juga di hook `after`), dan penutupan form dirty (langkah 38 sampai 40, S-08).
- Anchor absence (butir 8b.2): `Verifikasi` header, field, dan helper pada langkah 2 sampai 6 mendahului langkah 7; langkah 14 dan 15 mendahului langkah 16.
- Nilai awal tiga field per Product diasersi satu `Verifikasi` per field (langkah 10 sampai 12, 18 sampai 20, 33 sampai 35).
- Ukuran: 41 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (screening dan nilai awal form Activate Trial), satu modal dibuka sekali untuk TC tanpa submit, dan jumlah langkah berasal dari Verifikasi per klausa Expected (S-01); pemecahan menambah seeding tanpa menambah isolasi.
- Anchor dropdown Plan kosong (butir 8b.2): langkah 23 memverifikasi dropdown Plan terbuka sebagai surface sebelum langkah 24 mengasersi tanpa opsi; ini bukan anchor data pembanding (lihat Temuan untuk QA TC-AC-CS-180).
- Temuan untuk QA:
  - TC-AC-CS-180 Expected a (dropdown Plan belum berisi opsi) tidak menyediakan anchor positif (opsi atau pesan kosong yang dapat diasersi) dan tidak menyebut teks empty state; spec hanya memverifikasi dropdown terbuka lalu mengasersi tanpa opsi. Pemilik TC perlu menambah anchor atau teks empty state.
  - TC-AC-CS-180 Expected b tidak menyebut daftar plan persis; spec mengasersi daftar plan Paid aktif Product `FAMS` berurut rank (isi dibaca lewat fixture).
  - TC-AC-CS-177 Expected (placeholder Log Source Quota SIEM "Enter log source quota") bertentangan dengan TC-AC-CS-181 Expected b (nilai awal Log Source Quota SIEM `10`): field dengan nilai awal `10` tidak menampilkan placeholder. Spec tetap mengasersi keduanya sesuai TC (langkah 14 dan 20); pemilik TC perlu memperjelas precondition (placeholder tampil sebelum nilai awal terisi atau setelah `[Clear Field]`).
  - TC-AC-CS-182 Precondition tidak menyebut cara mengubah ceiling Trial; ditulis sebagai fixture BE "disediakan tim FE/BE".
