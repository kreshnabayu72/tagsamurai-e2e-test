---
id: TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result
title: "Popup Assign: Pencarian Name, Email, Position, Division, Status, dan No Result"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-69
  - TC-GS-ROLE-70
  - TC-GS-ROLE-71
  - TC-GS-ROLE-72
  - TC-GS-ROLE-316
coverage:
  web: automated
---

# Popup Assign: Pencarian Name, Email, Position, Division, Status, dan No Result

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; popup hanya dibuka dan dicari.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): kandidat picker Pre-setup #11: Sari Wulandari (Active); Maya Anggraini (Staff, IT, Inactive; nama dan email tanpa kata "inactive"); Ahmad Fauzan `ahmad.fz@client.com` (IT Staff, IT) dan Ahmad Fauzan `ahmad.fauzan@client.com` (Warehouse Staff, Logistics). Pool memuat user dengan Status Active dan Inactive (dua nilai distinct pada kolom Status), dan user dengan Position serta Division berbeda-beda.
- Data uji kolom Curated: TAG `TG-00877` dan Region `Bandung` milik user di pool, Rudi Hartono (Pre-setup #11, Activation Status `Pending Activation`), dan sedikitnya satu user Temporary User `Yes` dengan Temporary Until terisi. Kolom Curated (Activation Status, Temporary User, Temporary Until, TAG, Custom Field aktif) default Hidden di picker; TC-GS-ROLE-71 mengasersi keyword `Pending`, `Yes`, `TG-00877`, `Bandung` tidak mencocokkan selagi kolom Hidden, lalu TC-GS-ROLE-316 mengaktifkan kolom lewat Setup Column dan mengasersi keyword yang sama mencocokkan. Prasyarat environment (tidak di-seed spec): Custom Field aktif `Region` (Dropdown) dengan opsi `Bandung`, dan sedikitnya satu user di pool picker ber-Region `Bandung` (pola seeding spec 062 dan 063, PATCH custom-fields modul User ke akun aktor, tidak dipakai di sini karena yang dicari adalah kandidat picker, bukan akun aktor Total Control; spec ini tidak mengubah data, sehingga pool tidak di-seed). User Temporary disediakan tim FE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- State yang diubah dan dipulihkan: konfigurasi kolom Popup Assign diubah di TC-GS-ROLE-316 dan dikembalikan ke default lewat `[Reset to Default]` lalu `[Save]` (langkah 49 sampai 51), hook `after` sebagai cadangan.
- Kemampuan teknis: membaca isi kolom tabel picker; Popup Setup Column picker. Locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum dipetakan (FE follow-up, lihat Notes).

## Test Steps

1. Klik `[+ Assign]`

### TC-GS-ROLE-69: No-result Search pada Popup Assign

2. Ketik Search `zzqx`, tekan Enter
3. Verifikasi Illustration empty state tampil
4. Verifikasi Title `No results found`
5. Verifikasi Description `Try adjusting your search or filter.`

### TC-GS-ROLE-70: Search Popup Assign berdasarkan Name dan Email

6. Ganti isi kotak search dengan `wula`, tekan Enter
7. Verifikasi baris Sari Wulandari tampil
8. Verifikasi tabel hanya memuat baris Sari Wulandari (substring pada Name)
9. Ganti isi kotak search dengan `AHMAD.FZ`, tekan Enter
10. Verifikasi baris Ahmad Fauzan (`ahmad.fz@client.com`) tampil
11. Verifikasi tabel hanya memuat baris Ahmad Fauzan (`ahmad.fz@client.com`) (cocok case-insensitive pada Email)

### TC-GS-ROLE-71: Search Popup Assign berdasarkan Position dan Division serta kolom yang tidak dicari

12. Ganti isi kotak search dengan `Warehouse`, tekan Enter
13. Verifikasi baris Ahmad Fauzan (Warehouse Staff) tampil (cocok pada Position)
14. Ganti isi kotak search dengan `logis`, tekan Enter
15. Verifikasi baris Ahmad Fauzan (Logistics) tampil (cocok pada Division)
16. Ganti isi kotak search dengan `TG-00877`, tekan Enter
17. Verifikasi `No results found` tampil (TAG tidak dicari, kolom masih Hidden, default)
18. Ganti isi kotak search dengan `Bandung`, tekan Enter
19. Verifikasi `No results found` tampil (Region tidak dicari, kolom masih Hidden, default)
20. Ganti isi kotak search dengan `Pending`, tekan Enter
21. Verifikasi `No results found` tampil (Activation Status tidak dicari, kolom masih Hidden, default)
22. Ganti isi kotak search dengan `Yes`, tekan Enter
23. Verifikasi `No results found` tampil (Temporary User tidak dicari, kolom masih Hidden, default)

### TC-GS-ROLE-72: Search Popup Assign mencocokkan kolom Status

24. Ganti isi kotak search dengan `inactive`, tekan Enter
25. Verifikasi baris Maya Anggraini (Status Inactive) tampil
26. Verifikasi baris Sari Wulandari (Status Active) tidak tampil

### TC-GS-ROLE-316: Search Popup Assign mencakup kolom Curated yang diaktifkan lewat Setup Column

27. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
28. Centang kolom Activation Status
29. Centang kolom Temporary User
30. Centang kolom Temporary Until
31. Centang kolom TAG
32. Centang kolom Region
33. Klik `[Save]`
34. Verifikasi kolom Activation Status tampil di tabel picker
35. Verifikasi kolom Temporary User tampil di tabel picker
36. Verifikasi kolom Temporary Until tampil di tabel picker
37. Verifikasi kolom TAG tampil di tabel picker
38. Verifikasi kolom Region tampil di tabel picker
39. Ganti isi kotak search dengan `Pending`, tekan Enter
40. Verifikasi baris Rudi Hartono (Activation Status `Pending Activation`) tampil
41. Ganti isi kotak search dengan `Yes`, tekan Enter
42. Verifikasi baris user dengan Temporary User `Yes` tampil
43. Ganti isi kotak search dengan `TG-00877`, tekan Enter
44. Verifikasi baris user ber-TAG `TG-00877` tampil
45. Ganti isi kotak search dengan `Bandung`, tekan Enter
46. Verifikasi baris user Region `Bandung` tampil
47. Ganti isi kotak search dengan tanggal yang tampil di kolom Temporary Until (dibaca dari baris Temporary User `Yes`), tekan Enter
48. Verifikasi `No results found` tampil (kolom tanggal tidak dicari)
49. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
50. Klik `[Reset to Default]`
51. Klik `[Save]`
52. Ganti isi kotak search dengan `TG-00877`, tekan Enter
53. Verifikasi `No results found` tampil (kolom TAG kembali Hidden)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Satu pembukaan popup; tiap pencarian mengganti isi kotak search sebelumnya (bagian 8b butir 9). Urutan TC sumber dipertahankan.
- Asersi absence (langkah 17, 19, 21, 23, dan 26) memakai empty state `No results found` sebagai anchor positif bagi hasil Search, dan langkah 25 sebagai anchor positif bagi langkah 26 (baris pembanding pada surface yang sama).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 27 sampai 33 (menampilkan kolom Curated lewat Setup Column, mengamati Expected a sampai d TC-GS-ROLE-316) dan langkah 49 sampai 51 (`[Reset to Default]` lalu `[Save]`, Langkah Uji 8 TC-GS-ROLE-316). TC-GS-ROLE-316 ditaruh sesudah TC-GS-ROLE-71 karena TC-GS-ROLE-71 mengasersi kolom Curated masih Hidden (default), dan konfigurasi kolom dikembalikan ke default di langkah 49 sampai 51.
- Spec melewati sekitar 35 langkah (53 langkah) karena TC-GS-ROLE-316 menambah blok Setup Column (lima kolom dicentang satu per satu, lima `Verifikasi` kolom tampil sebagai anchor positif hasil Search, S-01) di atas empat TC Search yang sudah ada. Semua blok satu kelas harness (fungsional Search picker), satu popup, satu akun; kegagalan blok TC-GS-ROLE-316 tidak membuat asersi TC-GS-ROLE-69 sampai 72 kehilangan makna karena blok itu berjalan terakhir.
- Pembagian TC lintas spec: TC-GS-ROLE-51, 52, 53, 77 ada di spec 023; TC-GS-ROLE-54 sampai 57 ada di spec 024; TC-GS-ROLE-73, 74 ada di spec 026; TC-GS-ROLE-75, 76, 293, 317 ada di spec 027.
- Temuan untuk QA:
  - TC-GS-ROLE-71 Expected c sampai e menulis "tidak cocok" tanpa menyebut baris spesifik; spec memakai empty state `No results found` sebagai bukti tidak ada baris cocok, dengan asumsi tidak ada kolom lain di pool yang cocok dengan keyword.
  - TC-GS-ROLE-71 tidak menyebut user pemilik TAG `TG-00877` dan Region `Bandung`; keberadaan user ber-Region `Bandung` di pool adalah prasyarat environment (lihat Prerequisites; seeding via API modul User tidak mencukupi untuk kandidat picker). TAG `TG-00877` dan user Temporary disediakan tim FE.
  - TC-GS-ROLE-71 langkah 6 menggabungkan dua pencarian (`Pending`, lalu `Yes`); spec memisahkannya menjadi dua langkah dengan `Verifikasi` masing-masing.
  - TC-GS-ROLE-316 Langkah Uji 7 ("tanggal yang tampil di kolom Temporary Until") tidak menyebut nilai; spec membaca tanggal dari baris Temporary User `Yes`. TC-GS-ROLE-316 Expected b dan c tidak menyebut nama user pemilik Temporary User `Yes` dan TAG `TG-00877`; asersi memakai baris yang tersedia di environment (user Temporary `Yes` dan TAG `TG-00877` disediakan tim FE; user Region `Bandung` prasyarat environment).
  - FE follow-up: locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum ada di Page Object; langkah 27 dan 49 memakai deskripsi UI sampai tim FE memetakannya.
