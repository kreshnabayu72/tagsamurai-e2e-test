---
id: TC-AC-PP-E2E-025-publish-berhasil-immutability
title: "Publish New Version Berhasil: Badge Active Berpindah, Jalur View, Tiga Publikasi, dan Pemulihan Manual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-75
  - TC-AC-PP-76
  - TC-AC-PP-77
  - TC-AC-PP-78
coverage:
  web: automated
---

# Publish New Version Berhasil: Badge Active Berpindah, Jalur View, Tiga Publikasi, dan Pemulihan Manual

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026 dengan paragraf `Old policy text for version two.`; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); Fixture BE yang sama dipakai untuk membuat ulang Riwayat A di antara TC; hook `after` mengembalikan dataset ke Riwayat A.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish enam versi (ditambah pembuatan ulang dataset); suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini). Tanggal hari ini pada baris versi baru mengikuti Date Format ini.
- Kemampuan teknis: Fixture BE (di atas); menyalin (Ctrl+A, Ctrl+C) konten dari Modal View dan menempelkannya ke editor (izin clipboard browser).

## Test Steps

### TC-AC-PP-75: Publish New Version dari baris Active menghasilkan versi baru yang langsung Active dan badge berpindah

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Ketik " Updated terms." di akhir konten
4. Klik `[Publish New Version]`
5. Klik `[Publish]`
6. Verifikasi muncul toast sukses "Success, Privacy Policy has been published."
7. Verifikasi Dialog Publish Confirm tertutup
8. Verifikasi Modal tertutup
9. Verifikasi kembali ke tabel Version History
10. Verifikasi tidak ada dialog tambahan
11. Verifikasi tabel menampilkan 4 baris
12. Verifikasi baris teratas adalah `Version 4` dengan badge `Active`
13. Verifikasi Published At baris `Version 4` adalah tanggal hari ini
14. Verifikasi Published By baris `Version 4` adalah `Andi W`
15. Verifikasi badge `Active` tidak lagi ada pada `Version 3`
16. Verifikasi `Version 3` tanpa badge
17. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-76: Publish New Version lewat jalur View → [Edit] menghasilkan versi baru yang sama

18. Klik teks tautan `Version 3`
19. Klik `[Edit]` di footer
20. Tunggu konten editor termuat
21. Ketik " Via view path." di akhir konten
22. Klik `[Publish New Version]`
23. Klik `[Publish]`
24. Verifikasi toast sukses "Success, Privacy Policy has been published."
25. Verifikasi Dialog Publish Confirm tertutup
26. Verifikasi Modal tertutup
27. Verifikasi tabel menampilkan `Version 4` dengan badge `Active` di baris teratas
28. Klik teks tautan `Version 4`
29. Verifikasi konten Modal View `Version 4` adalah konten Version 3 ditambah " Via view path."
30. Klik `✕` di header untuk menutup Modal View
31. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-77: Publish tidak mengubah isi versi lama dan nomor versi bertambah berurutan pada tiga publikasi berturut-turut

32. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
33. Tunggu konten editor termuat
34. Ketik " Rev A." di akhir konten
35. Klik `[Publish New Version]`
36. Klik `[Publish]`
37. Klik `[⋯]` pada baris Active (`Version 4`) → pilih `Edit`
38. Tunggu konten editor termuat
39. Ketik " Rev B." di akhir konten
40. Klik `[Publish New Version]`
41. Klik `[Publish]`
42. Klik `[⋯]` pada baris Active (`Version 5`) → pilih `Edit`
43. Tunggu konten editor termuat
44. Ketik " Rev C." di akhir konten
45. Klik `[Publish New Version]`
46. Klik `[Publish]`
47. Verifikasi tabel menampilkan `Version 6` (Active), `Version 5`, `Version 4`, `Version 3`, `Version 2`, `Version 1` secara berurutan tanpa nomor loncat
48. Verifikasi hanya `Version 6` yang memiliki badge `Active`
49. Klik teks tautan `Version 3`
50. Verifikasi konten Version 3 identik dengan konten awal (tanpa " Rev A.")
51. Klik `✕` di header untuk menutup Modal View
52. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-78: Memulihkan isi versi lama dilakukan manual lewat salin dari View lalu tempel ke editor dan Publish sebagai versi baru

53. Klik teks tautan `Version 2`
54. Pilih seluruh konten Modal View lalu salin
55. Verifikasi footer Modal View `Version 2` kosong
56. Verifikasi tidak ada tombol Restore atau Salin di Modal View `Version 2`
57. Klik `✕` di header untuk menutup Modal View
58. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
59. Tunggu konten editor termuat
60. Klik `[Clear Field]`
61. Tempel konten yang disalin
62. Klik `[Publish New Version]`
63. Klik `[Publish]`
64. Verifikasi toast sukses "Success, Privacy Policy has been published."
65. Verifikasi `Version 4` berbadge `Active`
66. Klik teks tautan `Version 4`
67. Verifikasi Modal View `Version 4` menampilkan `Old policy text for version two.`
68. Klik `✕` di header untuk menutup Modal View
69. Klik teks tautan `Version 2`
70. Verifikasi konten `Version 2` tetap `Old policy text for version two.`
71. Klik `✕` di header untuk menutup Modal View
72. Klik teks tautan `Version 3`
73. Verifikasi konten `Version 3` tetap konten awal (H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`)
74. Klik `✕` di header untuk menutup Modal View

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor. TC mengharapkan `Version 3` Active dan menerbitkan `Version 4` pada tiap TC; karena tiap TC mem-publish, dataset dikembalikan ke Riwayat A lewat Fixture BE sebagai langkah penghubung (langkah 17, 31, 52) dan di hook `after`.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 17, 31, 52 (mengembalikan Riwayat A), langkah 30, 51, 57, 68, 71, 74 (menutup Modal View yang bersih tanpa dialog).
- TC-AC-PP-77 langkah 1-3 ("Publish dengan menambah teks ...") ditulis penuh sebagai tiga rangkaian Edit → ketik → `[Publish New Version]` → `[Publish]` (S-04). Baris Active pada Edit ke-2 dan ke-3 adalah `Version 4` dan `Version 5` yang baru terbit.
- Asersi tambahan yang dicatat: langkah 69-73 membuka `Version 2` dan `Version 3` untuk mengamati Expected d TC-AC-PP-78 ("Version 2 dan 3 tidak berubah") yang tidak punya langkah observasi di TC; langkah 13-16 memecah Expected c-d TC-AC-PP-75 menjadi satu `Verifikasi` per klausa; Expected a-b TC-AC-PP-75 dan TC-AC-PP-76 juga dipecah per klausa (mis. langkah 8-10 dan 25-26).
- Jumlah langkah (74) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan empat TC satu topik (Publish berhasil) dalam satu kelas harness; tiap blok `###` di-reseed ke Riwayat A lewat Fixture BE sehingga tetap bermakna walau blok sebelumnya gagal, dan spec tidak dipecah.
- Post Condition TC-AC-PP-75 butir c (modul terdampak Auth membaca nomor versi aktif `4` pada login berikutnya) dan butir d (record audit Publish) tanpa langkah observasi di TC tidak diasersi; efek ke Auth diuji di `auth/login-password/TestCases/tc-login-password.md` dan log Publish diuji di spec log (TC-AC-PP-154 dan 155). Post Condition TC-AC-PP-76, 77, 78 tanpa langkah observasi juga tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-77 langkah 1-3 ("Publish dengan menambah teks ...") tidak menyebut jalur Edit-nya; spec memakai jalur row action `Edit` pada baris Active.
  - TC-AC-PP-78 langkah 1 ("pilih seluruh konten lalu salin") tidak menyebut cara menyalin; script perlu memutuskan mekanisme salin dan tempel (clipboard browser).
