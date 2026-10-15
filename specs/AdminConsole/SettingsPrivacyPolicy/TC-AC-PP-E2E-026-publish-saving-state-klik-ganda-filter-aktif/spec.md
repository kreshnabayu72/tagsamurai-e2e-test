---
id: TC-AC-PP-E2E-026-publish-saving-state-klik-ganda-filter-aktif
title: "Publish: State Publishing, Klik Ganda [Publish], dan Versi Baru Saat Filter Aktif"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-80
  - TC-AC-PP-81
  - TC-AC-PP-200
coverage:
  web: automated
---

# Publish: State Publishing, Klik Ganda [Publish], dan Versi Baru Saat Filter Aktif

## Prerequisites

- Mode: FE+BE. `Spectra.intercept()` dipakai di atas backend nyata untuk menahan respons Publish sampai dilepas di langkah 21 (TC-AC-PP-80 menyebut penahanan 5 detik; rangkaian aksi pada langkah 11-19 membutuhkan penahanan sampai dilepas, bukan batas waktu tetap) dan untuk mengamati jumlah request Publish yang terkirim (TC-AC-PP-81); intercept dilepas di langkah spec dan dipulihkan di hook `after` bila spec gagal di tengah.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); Fixture BE yang sama membuat ulang Riwayat A di antara TC; hook `after` mengembalikan dataset ke Riwayat A.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish tiga versi; suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Riwayat browser: hook `before` membuka halaman lain sebelum Settings > Privacy Policy sehingga Browser Back punya halaman tujuan (TC-AC-PP-80).
- Kemampuan teknis: Fixture BE; `Spectra.intercept()` untuk menahan respons dan menghitung request; klik ganda cepat (dua klik beruntun) pada `[Publish]`; Browser Back; tombol Esc; klik pada area gelap di luar dialog.

## Test Steps

### TC-AC-PP-80: Selama Publishing tombol Dialog dinonaktifkan, Esc dan klik luar diabaikan, dan Browser Back diblok

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Ketik " Slow publish." di akhir konten
4. Klik `[Publish New Version]`
5. Atur intercept untuk menahan respons Publish selama 5 detik
6. Klik `[Publish]`
7. Verifikasi Dialog Publish Confirm tetap terbuka
8. Verifikasi `[Publish]` disabled
9. Verifikasi `[Publish]` menampilkan spinner
10. Verifikasi `[Cancel]` disabled
11. Tekan Esc
12. Verifikasi Dialog Publish Confirm tetap terbuka (Esc diabaikan)
13. Klik area gelap di luar dialog
14. Verifikasi Dialog Publish Confirm tetap terbuka (klik luar diabaikan)
15. Klik `[Clear Field]` pada modal di belakang dialog
16. Verifikasi konten editor di belakang dialog tidak berubah (modal tidak merespons klik `[Clear Field]`)
17. Klik `✕` pada modal di belakang dialog
18. Verifikasi modal di belakang dialog tidak merespons klik `✕`
19. Klik Browser Back
20. Verifikasi halaman tidak berpindah
21. Lepas intercept sehingga respons Publish dilepaskan
22. Verifikasi Publish selesai dengan toast sukses "Success, Privacy Policy has been published."
23. Verifikasi Dialog Publish Confirm tertutup
24. Verifikasi Modal tertutup
25. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-81: Klik ganda [Publish] pada Dialog Publish Confirm hanya membuat satu versi baru

26. Atur intercept untuk menghitung request Publish yang terkirim tanpa mengubah respons
27. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
28. Tunggu konten editor termuat
29. Ketik " Double click." di akhir konten
30. Klik `[Publish New Version]`
31. Klik `[Publish]` dua kali dengan cepat
32. Verifikasi hanya satu toast sukses "Success, Privacy Policy has been published."
33. Verifikasi tabel menampilkan `Version 4` Active
34. Verifikasi tidak ada `Version 5`
35. Verifikasi klik kedua tidak mengirim permintaan kedua (jumlah request Publish = 1)
36. Lepas intercept penghitung request Publish
37. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-200: Versi baru yang tidak cocok dengan filter aktif tidak muncul di tabel terfilter setelah Publish

38. Klik icon Filter di toolbar
39. Pada field `Published By` centang `John Doe`
40. Klik `[Apply]`
41. Verifikasi tabel menampilkan `Version 3` dan `Version 2` (kondisi awal TC)
42. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
43. Tunggu konten editor termuat
44. Ketik " Filtered publish." di akhir konten
45. Klik `[Publish New Version]`
46. Klik `[Publish]`
47. Verifikasi toast sukses "Success, Privacy Policy has been published."
48. Verifikasi tabel tetap terfilter dan hanya menampilkan `Version 3` dan `Version 2`
49. Verifikasi `Version 4` (`Andi W`) tidak tampil di tabel
50. Verifikasi tidak ada badge `Active` di tabel
51. Buka panel Filter
52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Verifikasi `Version 4` tampil di baris teratas dengan badge `Active`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor. Tiap TC membuat `Version 4` dari `Version 3` Active, sehingga dataset dikembalikan ke Riwayat A lewat Fixture BE sebagai langkah penghubung (langkah 25 dan 37) dan di hook `after`.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 21 (melepas intercept penahan respons, S-09), langkah 25 dan 37 (mengembalikan Riwayat A), langkah 26 dan 36 (memasang dan melepas intercept penghitung request), langkah 38-40 (menerapkan filter sebagai kondisi awal TC-AC-PP-200 yang tertulis di Precondition TC).
- Asersi tambahan yang dicatat: langkah 41 memverifikasi kondisi awal Precondition TC-AC-PP-200 (tabel menampilkan `Version 3` dan `Version 2` setelah filter); langkah 16 dan 18 menerjemahkan Expected b TC-AC-PP-80 ("modal di belakang tidak merespons klik `[Clear Field]`, `[✕]`") dan langkah 11-14 menerjemahkan "Esc dan klik luar diabaikan"; Esc pada modal di belakang dialog tercakup oleh langkah 11-12 (Esc yang ditekan saat dialog terbuka diabaikan, modal di belakang tidak tertutup).
- Jumlah langkah (54) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan tiga TC satu topik (Publish) dalam satu kelas harness; tiap blok `###` di-reseed ke Riwayat A lewat Fixture BE sehingga tetap bermakna walau blok sebelumnya gagal, dan spec tidak dipecah.
- Post Condition TC ("Version 4 tersimpan satu kali", "Hanya Version 4 yang tersimpan", "Version 4 tersimpan") tanpa langkah observasi tidak diasersi, kecuali yang sudah menjadi Expected (langkah 33-34). Klausa "disabled dengan spinner" pada Expected a TC-AC-PP-80 dipecah menjadi dua `Verifikasi` (langkah 8-9, S-01).
- Temuan untuk QA:
  - TC-AC-PP-80 Expected b menyatakan modal di belakang "tidak merespons ... Esc" terpisah dari Esc pada dialog; karena Esc hanya satu tombol fisik, spec memverifikasinya melalui satu langkah Esc (langkah 11) dengan Expected dialog tetap terbuka.
  - TC-AC-PP-81 Expected c ("Klik kedua tidak mengirim permintaan kedua") butuh cara menghitung request Publish; spec memakai intercept penghitung (langkah 26, 35). Cara hitung request tidak dinyatakan di TC.
  - TC-AC-PP-200 Precondition menyebut Filter `Published By` = `John Doe` sudah ter-Apply tetapi tidak menyebut langkah penerapannya; spec menulis langkah 38-40.
