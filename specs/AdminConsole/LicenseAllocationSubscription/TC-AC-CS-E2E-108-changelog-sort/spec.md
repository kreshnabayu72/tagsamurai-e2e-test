---
id: TC-AC-CS-E2E-108-changelog-sort
title: "Changelog: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-419
  - TC-AC-CS-420
  - TC-AC-CS-421
coverage:
  web: automated
---

# Changelog: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- Tabel "Kolom sort" (TC-AC-CS-419): `Action`, `Client — Product`, `Field`.

## Test Steps

1. Klik ikon Changelog di toolbar
2. Verifikasi tabel Changelog menampilkan sedikitnya satu entri

### TC-AC-CS-419: Siklus sort tiga state kolom teks Action, Client — Product, Field

3. Untuk setiap baris tabel "Kolom sort" (langkah 3 sampai 8): klik header kolom itu sekali
4. Verifikasi kolom itu terurut ascending A-Z
5. Klik header kolom itu sekali lagi
6. Verifikasi kolom itu terurut descending Z-A
7. Klik header kolom itu sekali lagi
8. Verifikasi tabel kembali ke default Date Newest First
9. Klik header `Client — Product` sekali
10. Verifikasi `Client — Product` diurutkan berdasarkan string gabungan
11. Klik header `Client — Product` dua kali lagi untuk kembali ke default

### TC-AC-CS-420: Sort kolom campuran Old Value dan New Value menaruh kosong di akhir saat ascending

12. Klik header `Old Value` satu kali
13. Pindah ke halaman terakhir
14. Verifikasi Old Value ascending menaruh entri bernilai kosong `—` di akhir
15. Pindah ke halaman pertama
16. Klik header `New Value` satu kali
17. Verifikasi `New Value` terurut ascending
18. Klik header `New Value` sekali lagi
19. Verifikasi `New Value` terurut descending
20. Klik header `New Value` sekali lagi
21. Verifikasi tabel kembali ke default Date Newest First
22. Klik header `Old Value` dua kali lagi untuk kembali ke default

### TC-AC-CS-421: Sort Modified By memakai nama lengkap, bukan format singkat

23. Klik header `Modified By` sekali
24. Verifikasi urutan ascending mengikuti nama lengkap user: `Budi S` (Budi Santoso), `Dewi A` (Dewi Anggraini), `Fajar N` (Fajar Nugroho), `Hendra W` (Hendra Wijaya), `Maya T` (Maya Tanjung), `Rina P` (Rina Pratama), lalu `System`, dan bukan teks singkat yang tampil
25. Verifikasi entri `System` mengikuti aturan huruf besar kecil kolom teks
26. Klik header `Modified By` dua kali lagi untuk kembali ke default

## Notes

- Langkah berulang per kolom: langkah 3 sampai 8 (tiga iterasi: `Action`, `Client — Product`, `Field`); parameter iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat.
- Alasan spec lebih dari sekitar 35 langkah: nominal 26 langkah menjadi 38 setelah ekspansi (langkah 3 sampai 8 diulang tiga kali). Ketiga TC memakai satu modal Changelog dan satu dataset seed #84; blok per kolom diulang dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah klik header yang mengembalikan sort ke default (S-09) dan langkah klik ikon Changelog untuk membuka modal.
- Sort memakai data seed #84 dengan lebih dari dua nilai distinct pada tiap kolom yang diurutkan (S-11); urutan posisi hanya diasersi atas entri seed pada keadaan yang dipulihkan baseline (S-14).
- Temuan untuk QA:
  - TC-AC-CS-421 Expected b ("Entri `System` mengikuti aturan huruf besar kecil kolom teks") tidak menyebut aturan huruf besar kecil yang dimaksud; spec menuliskannya apa adanya.
  - TC-AC-CS-420 Expected a tidak menyebut urutan descending untuk Old Value; spec hanya mengasersi ascending sesuai TC.
