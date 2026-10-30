---
id: TC-GS-ROLE-E2E-032-konflik-assign-alert-jamak-user-tidak-eligible-dan-campuran
title: "Konflik Assign: Alert Jamak User Tidak Eligible dan Campuran Dihapus dan Tidak Eligible"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-301
  - TC-GS-ROLE-302
  - TC-GS-ROLE-305
coverage:
  web: automated
---

# Konflik Assign: Alert Jamak User Tidak Eligible dan Campuran Dihapus dan Tidak Eligible

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (c), dua admin; objek uji adalah alert di sesi A setelah admin kedua membuat beberapa user tidak eligible atau menghapusnya.
- Akun aktor sesi A (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Admin kedua: Eko Prasetyo (Total Control, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Eko hanya memicu perubahan state lewat sesi API (tanpa sesi UI kedua).
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-032`; kandidat Pre-setup #11 dengan state kandidat: Active, Access Global Settings dicentang, tanpa access level, tanpa baris role):
  - Ahmad Fauzan (`ahmad.fz@client.com`): tidak diubah; tetap tercentang di picker.
  - Ahmad Fauzan (`ahmad.fauzan@client.com`): di-assign Total Control sesi API Eko di TC-GS-ROLE-305.
  - Nina Kartika dan Wawan Setiawan: di-assign Total Control sesi API Eko di TC-GS-ROLE-301 dan TC-GS-ROLE-305; Nina Kartika dihapus dan Wawan Setiawan di-assign Total Control sesi API Eko di TC-GS-ROLE-302.
- Pemulihan: langkah penghubung sesi API Eko mencabut access level Total Control dan membuat ulang user yang dihapus sebagai kandidat (langkah 11, 22, dan 35) dan hook `after` menjadi cadangan.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): klien HTTP terotentikasi sebagai Eko Prasetyo untuk meng-assign Total Control, menghapus user, mencabut access level, dan membuat ulang user kandidat.

## Test Steps

### TC-GS-ROLE-301: Assign Total Control saat dua user terpilih menjadi tidak eligible sebelum submit (alert jamak)

1. Klik `[+ Assign]`
2. Centang Ahmad Fauzan (`ahmad.fz@client.com`), Nina Kartika, dan Wawan Setiawan
3. Sesi API Eko: assign Total Control ke Nina Kartika dan Wawan Setiawan
4. Klik `[Assign]`
5. Verifikasi alert inline (danger) jamak satu kalimat dengan pola `[User Names] are no longer eligible. Please select another.` tampil dan menyebut kedua nama Nina Kartika dan Wawan Setiawan (urutan nama tidak diasersi)
6. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tercentang
7. Verifikasi counter `1 user selected` tampil (centangan Nina Kartika dan Wawan Setiawan hilang)
8. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
9. Verifikasi Nina Kartika dan Wawan Setiawan tidak tampil di picker setelah picker di-refetch
10. Klik `[Cancel]`
11. Sesi API Eko: cabut access level Total Control dari Nina Kartika dan Wawan Setiawan

### TC-GS-ROLE-305: Assign Total Control saat tiga user terpilih menjadi tidak eligible sebelum submit (alert jamak ≥3)

12. Klik `[+ Assign]`
13. Centang Ahmad Fauzan (`ahmad.fz@client.com`), Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan
14. Sesi API Eko: assign Total Control ke Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan
15. Klik `[Assign]`
16. Verifikasi alert inline (danger) satu kalimat dengan pola `[User Names] are no longer eligible. Please select another.` tampil dan menyebut ketiga nama Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan dengan koma dan `and` sebelum nama terakhir (urutan nama tidak diasersi)
17. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tercentang
18. Verifikasi counter `1 user selected` tampil (centangan ketiga user hilang)
19. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
20. Verifikasi Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan tidak tampil di picker setelah picker di-refetch
21. Klik `[Cancel]`
22. Sesi API Eko: cabut access level Total Control dari Ahmad Fauzan (`ahmad.fauzan@client.com`), Nina Kartika, dan Wawan Setiawan

### TC-GS-ROLE-302: Assign Total Control dengan campuran user dihapus dan user tidak eligible dalam satu submit

23. Klik `[+ Assign]`
24. Centang Ahmad Fauzan (`ahmad.fz@client.com`), Nina Kartika, dan Wawan Setiawan
25. Sesi API Eko: hapus user Nina Kartika di modul User
26. Sesi API Eko: assign Total Control ke Wawan Setiawan
27. Klik `[Assign]`
28. Verifikasi alert inline (danger) V-10 `Nina Kartika no longer exists. Please select another.` tampil
29. Verifikasi alert V-11 untuk Wawan Setiawan (`Wawan Setiawan is no longer eligible. Please select another.`) tidak tampil
30. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tercentang
31. Verifikasi counter `1 user selected` tampil (centangan Nina Kartika dan Wawan Setiawan hilang)
32. Verifikasi Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
33. Verifikasi Nina Kartika tidak tampil di picker setelah picker di-refetch
34. Klik `[Cancel]`
35. Sesi API Eko: buat ulang user Nina Kartika sebagai kandidat dan cabut access level Total Control dari Wawan Setiawan

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (c), dua admin, satu spec untuk satu jenis harness.
- `P-2`: Eko Prasetyo hanya memicu perubahan state (assign Total Control, hapus user) lewat sesi API dan bukan objek asersi; tidak ada sesi UI kedua. Objek asersi tetap sesi A.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec berjumlah 35 langkah, tepat di ambang sekitar 35. Ketiga TC satu kelas harness dan satu layar, tiap blok dimulai dari popup baru dan dipulihkan oleh sesi API Eko di antara blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah (301, 305, 302): TC-GS-ROLE-302 yang menghapus user diletakkan paling akhir (bagian 3 prinsip 5).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `[Cancel]` menutup popup (langkah 10, 21, 34) dan pemulihan sesi API Eko (langkah 11, 22, 35).
- Asersi tambahan di luar kalimat Expected TC (S-03): "Ahmad Fauzan (`ahmad.fz@client.com`) tetap tampil di picker" (langkah 8, 19, 32) membuktikan Expected "submit ditolak seluruhnya, Ahmad Fauzan tidak menjadi Total Control" karena pool picker hanya memuat user tanpa access level; langkah 6, 17, dan 30 menjadi anchor positif bagi asersi absence di picker (langkah 9, 20, 33; bagian 8b butir 2). Langkah 29 (alert V-11 tidak tampil) didahului alert V-10 pada langkah 28 sebagai anchor positif.
- Expected TC-GS-ROLE-302 d menyatakan picker di-refetch tanpa Nina Kartika (langkah 33); Wawan Setiawan ikut hilang dari pool karena menjadi Total Control, tetapi hal itu tidak diasersi karena tidak disebut Expected.
- Temuan untuk QA:
  - TC-GS-ROLE-301, 302, dan 305 menyebut "centang" tanpa cara menemukan baris bila picker lebih dari satu halaman; spec mengikuti TC dan mekanisme menemukan baris diputuskan di tahap script.
  - Tabel Dinamis #6 (Kandidat) mencantumkan TC-GS-ROLE-301 dan TC-GS-ROLE-302 tetapi tidak TC-GS-ROLE-305 pada kolom "Digunakan di TC", padahal TC-GS-ROLE-305 memakai Nina Kartika, Wawan Setiawan, dan kedua Ahmad Fauzan; pemulihan Ahmad Fauzan (`ahmad.fauzan@client.com`) tidak tercantum.
  - Counter seleksi `1 user selected` diturunkan dari "centangan ... hilang" memakai teks counter TC-GS-ROLE-55; TC-GS-ROLE-301, 302, dan 305 tidak menyebut teks counter.
