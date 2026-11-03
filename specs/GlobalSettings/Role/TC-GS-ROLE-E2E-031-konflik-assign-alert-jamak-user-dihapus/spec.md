---
id: TC-GS-ROLE-E2E-031-konflik-assign-alert-jamak-user-dihapus
title: "Konflik Assign: Alert Jamak User Terpilih Dihapus Admin Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-300
  - TC-GS-ROLE-304
coverage:
  web: automated
---

# Konflik Assign: Alert Jamak User Terpilih Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (c), dua admin; objek uji adalah alert jamak di sesi A setelah admin kedua menghapus beberapa user.
- Akun aktor sesi A (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Admin kedua: Eko Prasetyo (Total Control, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Eko hanya memicu penghapusan user lewat sesi API (tanpa sesi UI kedua).
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-031`; kandidat Pre-setup #11 dengan state kandidat: Active, Access Global Settings dicentang, tanpa access level, tanpa baris role):
  - Ahmad Fauzan (`ahmad.fz@client.com`, IT Staff, IT): tidak diubah; tetap tercentang di picker.
  - Ahmad Fauzan (`ahmad.fauzan@client.com`, Warehouse Staff, Logistics): dihapus sesi API Eko di TC-GS-ROLE-304.
  - Nina Kartika dan Wawan Setiawan: dihapus sesi API Eko di TC-GS-ROLE-300 dan TC-GS-ROLE-304.
- Pemulihan: langkah penghubung sesi API Eko membuat ulang user yang dihapus sebagai kandidat (langkah 12 dan 23) dan hook `after` menjadi cadangan.
- Efek pemulihan yang tidak dikembalikan: penghapusan dan pembuatan ulang user lewat sesi API Eko meninggalkan efek pada Modified By, Last Updated, dan entri Changelog user kandidat (Nina Kartika, Wawan Setiawan, Ahmad Fauzan `ahmad.fauzan@client.com`) yang tidak dapat dipulihkan. Spec tidak mengasersi Modified By, Last Updated, maupun jumlah entri Changelog; bila asersi itu ditambahkan, memakai baseline jumlah entri sebelum aksi (S-12).
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): klien HTTP terotentikasi sebagai Eko Prasetyo untuk menghapus user dan membuat ulang user kandidat.

## Test Steps

### TC-GS-ROLE-300: Assign Total Control saat dua user terpilih dihapus admin lain sebelum submit (alert jamak)

1. Klik `[+ Assign]`
2. Centang Ahmad Fauzan (`ahmad.fz@client.com`), Nina Kartika, dan Wawan Setiawan
3. Sesi API Eko: hapus user Nina Kartika dan Wawan Setiawan di modul User hingga penghapusan tersimpan
4. Klik `[Assign]`
5. Verifikasi alert inline (danger) jamak satu kalimat dengan pola `[User Names] no longer exist. Please select another.` tampil dan menyebut kedua nama Nina Kartika dan Wawan Setiawan (urutan nama tidak diasersi)
6. Verifikasi popup Assign Total Control tetap terbuka
7. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tercentang
8. Verifikasi counter `1 user selected` tampil (centangan Nina Kartika dan Wawan Setiawan hilang)
9. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
10. Verifikasi Nina Kartika dan Wawan Setiawan tidak tampil di picker setelah picker di-refetch
11. Klik `[Cancel]`
12. Sesi API Eko: buat ulang user Nina Kartika dan Wawan Setiawan sebagai kandidat hingga user kandidat tersimpan

### TC-GS-ROLE-304: Assign Total Control saat tiga user terpilih dihapus admin lain sebelum submit (alert jamak ≥3)

13. Klik `[+ Assign]`
14. Centang Ahmad Fauzan (`ahmad.fz@client.com`), Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan
15. Sesi API Eko: hapus user Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan di modul User hingga penghapusan tersimpan
16. Klik `[Assign]`
17. Verifikasi alert inline (danger) satu kalimat dengan pola `[User Names] no longer exist. Please select another.` tampil dan menyebut ketiga nama Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan dengan koma dan `and` sebelum nama terakhir (urutan nama tidak diasersi)
18. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tercentang
19. Verifikasi counter `1 user selected` tampil (centangan ketiga user hilang)
20. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
21. Verifikasi Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan tidak tampil di picker setelah picker di-refetch
22. Klik `[Cancel]`
23. Sesi API Eko: buat ulang user Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan sebagai kandidat hingga user kandidat tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (c), dua admin, satu spec untuk satu jenis harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `[Cancel]` menutup popup (langkah 11 dan 22) dan pemulihan sesi API Eko (langkah 12 dan 23).
- Asersi tambahan di luar kalimat Expected TC (S-03): "Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker" (langkah 9 dan 20) membuktikan Expected "submit ditolak seluruhnya, Ahmad Fauzan tidak menjadi Total Control" karena pool picker hanya memuat user tanpa access level; langkah 7 dan 18 menjadi anchor positif bagi asersi absence di picker (langkah 10 dan 21; bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-ROLE-300 dan TC-GS-ROLE-304 menyebut "centang" tanpa cara menemukan baris bila picker lebih dari satu halaman; spec mengikuti TC dan mekanisme menemukan baris diputuskan di tahap script.
  - TC-GS-ROLE-304 menghapus Ahmad Fauzan (`ahmad.fauzan@client.com`), tetapi Tabel Dinamis #6 (Kandidat) hanya mencantumkan Nina Kartika dan Wawan Setiawan dan tidak mencantumkan pemulihan Ahmad Fauzan tersebut atau TC-GS-ROLE-304 di kolom "Digunakan di TC"; spec membuatnya ulang sebagai kandidat.
  - Counter seleksi `1 user selected` diturunkan dari "centangan ... hilang" memakai teks counter TC-GS-ROLE-55; TC-GS-ROLE-300 dan TC-GS-ROLE-304 tidak menyebut teks counter.
  - Pola alert jamak tidak menyebut tanda baca persis untuk dua nama (TC-GS-ROLE-300); spec hanya mengasersi kedua nama dan pola `[User Names] no longer exist. Please select another.`.
