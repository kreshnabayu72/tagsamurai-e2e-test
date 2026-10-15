---
id: TC-AC-PP-E2E-031-idempotency-key-bentrok-409-dialog-d03
title: "Idempotency Publish: Key Bentrok 409 dan Dialog Konteks Unable to Publish"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-92
  - TC-AC-PP-93
  - TC-AC-PP-202
coverage:
  web: automated
---

# Idempotency Publish: Key Bentrok 409 dan Dialog Konteks Unable to Publish

## Prerequisites

- Mode: FE+BE (kelas b, fault injection: intercept parsial di atas backend nyata dan asersi state backend).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe`, Version 2 `John Doe`, Version 1 `Jane Smith` akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Riwayat append-only, jadi Fixture BE juga dipakai untuk mengembalikan dataset di antara blok TC (langkah penghubung).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis:
  - Fixture BE untuk membuat ulang dataset Riwayat A.
  - `Spectra.intercept()` pada permintaan Publish: (1) diteruskan ke server dengan respons dibuang (TC-AC-PP-92 langkah 1); (2) permintaan kedua memakai idempotency key yang sama dengan permintaan pertama dan body berbeda (TC-AC-PP-92 langkah 2; key dibaca dari permintaan pertama yang tertangkap intercept); (3) respons Publish dipaksa 409 (TC-AC-PP-93); (4) permintaan diteruskan ke server (Version 4 tersimpan) tetapi responsnya diganti 409 (TC-AC-PP-202). Intercept dilepas di langkah spec dan dipulihkan di hook `after`.
  - Menunggu waktu nyata 30 detik (batas waktu FE) satu kali (TC-AC-PP-92 langkah 1).
- Suite berjalan serial (`parallel: false`): dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish versi baru. Hook `after` memulihkan dataset ke Riwayat A.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-92: Key idempotency yang sama dengan konten berbeda ditolak 409 dan menampilkan Dialog konteks D-03

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
3. Klik di akhir konten editor lalu ketik " First body."
4. Klik `[Publish New Version]`
5. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server dan respons dibuang, agar key pertama tersimpan di server
6. Klik `[Publish]`
7. Tunggu batas waktu 30 detik sampai toast "Connection problem. Please try again." tampil dan Dialog Publish Confirm tertutup
8. Ganti intercept: permintaan Publish berikutnya memakai key yang sama dengan permintaan pertama dan body berbeda
9. Klik `[Publish New Version]`
10. Klik `[Publish]`
11. Verifikasi permintaan kedua ditolak server (409)
12. Verifikasi toast "Error, failed to publish Privacy Policy." tidak tampil
13. Verifikasi Dialog Publish Confirm sudah tertutup
14. Verifikasi Dialog konteks tampil dengan Title "Unable to publish"
15. Verifikasi body Dialog konteks "This request could not be processed. Please try again."
16. Verifikasi Dialog konteks hanya memiliki satu tombol `[OK]`
17. Verifikasi fokus awal pada `[OK]`
18. Klik `[OK]`
19. Verifikasi Dialog konteks tertutup
20. Verifikasi modal tetap di state Edit
21. Verifikasi teks ` First body.` dipertahankan di editor
22. Lepas intercept
23. Klik `[✕]` di header modal
24. Verifikasi Dialog "Unsaved Changes" tampil
25. Klik `[Leave]`
26. Verifikasi tabel hanya memuat `Version 4` dari permintaan pertama sebagai versi baru
27. Verifikasi tidak ada versi dari permintaan kedua (tidak ada `Version 5`)

### TC-AC-PP-93: Dialog konteks D-03: hanya ditutup lewat [OK], Esc setara OK, klik luar dan Back diabaikan, modal Edit tetap dan tabel di-refresh saat modal ditutup

28. Kembalikan dataset ke Riwayat A lewat Fixture BE, lalu buka Settings > Privacy Policy
29. Pasang intercept pada permintaan Publish: respons dipaksa 409
30. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
31. Klik di akhir konten editor lalu ketik " Conflict case."
32. Klik `[Publish New Version]`
33. Klik `[Publish]`
34. Verifikasi Dialog Publish Confirm tertutup
35. Verifikasi Dialog konteks tampil dengan Title "Unable to publish"
36. Verifikasi body Dialog konteks "This request could not be processed. Please try again."
37. Verifikasi Dialog konteks hanya memiliki satu tombol `[OK]`
38. Verifikasi fokus awal pada `[OK]`
39. Verifikasi tidak ada toast
40. Klik `[Clear Field]` pada modal Edit di belakang dialog
41. Verifikasi konten editor tidak berubah (` Conflict case.` tetap ada)
42. Klik `[✕]` pada modal Edit di belakang dialog
43. Verifikasi Dialog konteks tetap terbuka
44. Verifikasi modal Edit tidak tertutup
45. Klik area gelap di luar modal Edit di belakang dialog
46. Verifikasi Dialog konteks tetap terbuka
47. Klik area gelap di luar dialog
48. Verifikasi Dialog konteks tetap terbuka
49. Klik Browser Back
50. Verifikasi Dialog konteks tetap terbuka
51. Verifikasi halaman tidak berpindah
52. Tekan Esc
53. Verifikasi Dialog konteks tertutup (setara `[OK]`)
54. Verifikasi modal tetap di state Edit
55. Verifikasi teks ` Conflict case.` dipertahankan di editor
56. Klik `[✕]` di header modal
57. Verifikasi Dialog "Unsaved Changes" tampil
58. Klik `[Leave]`
59. Verifikasi modal tertutup
60. Verifikasi tabel Version History di-refresh
61. Verifikasi tidak ada versi baru di tabel
62. Lepas intercept

### TC-AC-PP-202: Setelah Dialog konteks D-03 ditutup lewat [OK], Publish berikutnya diperlakukan sebagai permintaan baru

63. Kembalikan dataset ke Riwayat A lewat Fixture BE, lalu buka Settings > Privacy Policy
64. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
65. Klik di akhir konten editor lalu ketik " Rotate key."
66. Klik `[Publish New Version]`
67. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server (Version 4 tersimpan) tetapi responsnya diganti 409
68. Klik `[Publish]`
69. Verifikasi Dialog konteks "Unable to publish" tampil
70. Verifikasi Dialog konteks memiliki tombol `[OK]`
71. Klik `[OK]`
72. Lepas intercept
73. Klik `[Publish New Version]` tanpa mengubah konten
74. Klik `[Publish]`
75. Verifikasi Dialog Publish Confirm tertutup
76. Verifikasi modal tertutup
77. Verifikasi toast netral "No changes to save." tampil
78. Verifikasi toast sukses "Success, Privacy Policy has been published." tidak tampil
79. Verifikasi tabel memuat `Version 4` sebagai versi baru
80. Verifikasi tidak ada `Version 5` di tabel

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness: b (fault injection), asersi state backend.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah membuka halaman di awal blok TC-AC-PP-92 dan langkah mengembalikan dataset ke Riwayat A lewat Fixture BE di awal blok TC-AC-PP-93 dan 202; langkah melepas intercept di akhir blok TC-AC-PP-92 dan 93; langkah memasang intercept 409 di awal blok TC-AC-PP-93 (di TC disebut di Precondition, dipindah ke awal blok). Penutupan modal dirty di blok TC-AC-PP-92 dan 93 mengikuti butir S-08: `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]` (TC menulis "klik `[✕]` lalu klik `[Leave]`").
- Langkah aksi klik `[Clear Field]`, `[✕]`, area gelap, Browser Back, dan Esc di blok TC-AC-PP-93 adalah aksi uji untuk Expected b dan c (modal di belakang tidak merespons klik, klik luar dan Back diabaikan); TC menulis hanya "Amati" dan "Klik area gelap ... Browser Back ... Esc" di langkah 2-3, sehingga aksi klik `[Clear Field]`, `[✕]`, dan area gelap modal diturunkan dari Expected b.
- TC-AC-PP-92 Expected d (tabel setelah modal ditutup) dibaca dari langkah 4 TC ("klik `[✕]` lalu klik `[Leave]` → amati tabel").
- Ukuran spec melewati sekitar 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tiga blok TC tidak saling bergantung (dataset dikembalikan ke Riwayat A di awal blok), satu kelas (b) dan satu topik (key idempotency dan Dialog konteks D-03), sehingga kegagalan satu blok tidak membuat blok lain tidak bermakna; spec tidak dipecah.
- Pembagian TC lintas spec: TC-AC-PP-91, 203, 206, 213, 214 (timeout dan retry) di spec `TC-AC-PP-E2E-030`; TC-AC-PP-94, 212 (masa berlaku key) di spec `TC-AC-PP-E2E-032`.
- Temuan untuk QA:
  - TC-AC-PP-92 langkah 2 menulis "permintaan Publish berikutnya memakai key yang sama dengan body berbeda" tanpa menyebut cara memaksanya; UI membuat key baru untuk konten yang berubah (lihat TC-AC-PP-203). Spec memakai intercept yang menimpa key dengan key permintaan pertama, dan nama header tidak ditulis karena tidak ada di `openapi.yaml` (NC-02).
  - TC-AC-PP-92 Post Condition ("tidak ada record audit tambahan dari permintaan kedua") tidak punya langkah observasi log sehingga tidak diasersi; TC-AC-PP-93 dan 202 punya Post Condition serupa (tidak ada record audit) tanpa langkah observasi log, juga tidak diasersi.
  - TC-AC-PP-93 Expected b menyebut modal "tidak merespons klik `[Clear Field]`, `[✕]`, maupun klik area gelap", tetapi tidak ada langkah aksi di kolom Langkah Uji; ditandai sebagai kekurangan langkah di TC sumber.
  - TC-AC-PP-93 Expected d (Esc setara `[OK]`) memuat dua klausa (dialog tertutup, modal tetap Edit dengan konten dipertahankan); keduanya diasersi terpisah.
