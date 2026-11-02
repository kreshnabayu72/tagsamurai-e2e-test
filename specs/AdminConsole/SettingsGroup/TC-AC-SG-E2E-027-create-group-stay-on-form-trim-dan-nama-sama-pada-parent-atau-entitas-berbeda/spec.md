---
id: TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda
title: "Create Group: Stay on Form, Trim, dan Nama Sama pada Parent atau Entitas Berbeda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-83
  - TC-AC-SG-85
  - TC-AC-SG-86
  - TC-AC-SG-89
  - TC-AC-SG-90
coverage:
  web: automated
---

# Create Group: Stay on Form, Trim, dan Nama Sama pada Parent atau Entitas Berbeda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Untuk TC-AC-SG-86: Total Control entitas `Distributor Pembanding` (Pre-setup #33) `totalControlPembanding_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_PEMBANDING_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control Principal; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data seed milik spec (entitas Principal, di-seed Fixture BE di hook `before`): `Region A-{runId}-027` (level 1) dengan anak `Branch 1-{runId}-027`; `Region C-{runId}-027` (level 1, tanpa anak); `Region B-{runId}-027` (level 1, nama yang sama akan dibuat di tree `Distributor Pembanding` pada TC-AC-SG-86). Nama TC `Region A`, `Branch 1`, `Region C`, dan `Region B` diganti nama bersuffix milik spec karena target aksi tulis tidak memakai node Pre-setup bersama (S-06).
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec | Dibuat di |
|---|---|---|---|
| TC-AC-SG-83 | `Region Trim` (diketik dengan spasi tepi) | `Region Trim-{runId}-027` | Principal, level 1 |
| TC-AC-SG-85 | `Branch 1` | `Branch 1-{runId}-027` | Principal, anak `Region C-{runId}-027` |
| TC-AC-SG-89 | `Region Baru 1` | `Region Baru 1-{runId}-027` | Principal, level 1 |
| TC-AC-SG-90 | `Region Baru 2`, `Region Baru 3` | `Region Baru 2-{runId}-027`, `Region Baru 3-{runId}-027` | Principal, level 1 |
| TC-AC-SG-86 | `Region B` | `Region B-{runId}-027` | `Distributor Pembanding`, level 1 |

- Kemampuan teknis: Fixture BE (seeding, pemulihan baseline, dan pembacaan jumlah group tree Principal untuk TC-AC-SG-86) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus seluruh group milik spec pada entitas Principal dan `Distributor Pembanding` lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-83: Group Name di-trim otomatis

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `   Region Trim-{runId}-027   ` (spasi di awal dan akhir) pada Group Name, klik `[Submit]`
3. Verifikasi group dibuat dengan nama `Region Trim-{runId}-027` tanpa spasi di awal dan akhir
4. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-85: Nama sama pada parent berbeda

5. Klik ikon `⋯` pada node `Region C-{runId}-027` di sidebar, lalu pilih "+ Add Subgroup"
6. Ketik `Branch 1-{runId}-027` pada Group Name (nama sudah ada di bawah `Region A-{runId}-027`) dan berhenti mengetik selama sekitar 500 ms
7. Verifikasi tidak ada error duplikat pada Group Name
8. Klik `[Submit]`
9. Verifikasi subgroup `Branch 1-{runId}-027` dibuat di bawah `Region C-{runId}-027`
10. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-89: Submit dengan Stay tidak tercentang menutup popup

11. Klik `[+] Group` di Sidebar Group Tree
12. Ketik `Region Baru 1-{runId}-027` pada Group Name, klik `[Submit]`
13. Verifikasi popup tertutup
14. Verifikasi toast sukses: "Success, group has been created."
15. Verifikasi node `Region Baru 1-{runId}-027` tampil sebagai node level 1 di sidebar
16. Ketik Search `Region Baru 1-{runId}-027`, tekan Enter
17. Verifikasi baris `Region Baru 1-{runId}-027` tampil di tabel All Groups
18. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-90: Submit dengan Stay tercentang

19. Klik `[+] Group` di Sidebar Group Tree
20. Centang "Stay on this form after submitting"
21. Ketik `Region Baru 2-{runId}-027` pada Group Name, klik `[Submit]`
22. Verifikasi toast sukses: "Success, group has been created."
23. Verifikasi field Group Name kosong
24. Verifikasi popup tetap terbuka
25. Tunggu toast lama hilang otomatis
26. Ketik `Region Baru 3-{runId}-027` pada Group Name, klik `[Submit]`
27. Verifikasi toast sukses: "Success, group has been created."
28. Verifikasi field Group Name kosong
29. Verifikasi popup tetap terbuka
30. Verifikasi node `Region Baru 2-{runId}-027` dan `Region Baru 3-{runId}-027` tampil di sidebar
31. Hilangkan centang "Stay on this form after submitting", lalu klik `[✕]` pada popup

### TC-AC-SG-86: Nama sama pada entitas lain

32. Ganti akun: logout, lalu login sebagai Total Control entitas `Distributor Pembanding` (`totalControlPembanding_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_PEMBANDING_PASSWORD`)
33. Buka halaman `Settings > Group` lewat sidebar
34. Catat jumlah group tree Principal lewat Fixture BE sebagai baseline
35. Klik `[+] Group` di Sidebar Group Tree
36. Ketik `Region B-{runId}-027` pada Group Name (nama sudah ada pada tree Principal), berhenti mengetik sekitar 500 ms
37. Verifikasi tidak ada error duplikat pada Group Name
38. Klik `[Submit]`
39. Verifikasi group `Region B-{runId}-027` dibuat di tree `Distributor Pembanding`
40. Verifikasi toast sukses: "Success, group has been created."
41. Verifikasi jumlah group tree Principal (dibaca lewat Fixture BE) sama dengan baseline langkah 34 (tree Principal tidak berubah)

## Notes

- Urutan TC pada spec: TC-AC-SG-83, 85, 89, 90, 86. TC-AC-SG-86 diletakkan terakhir karena membutuhkan ganti akun ke entitas lain (hook `after` memulihkan sesi).
- Langkah penghubung (S-03): langkah 16 dan 18 (Search untuk menemukan baris target dan reset Search, R-16 dan S-09), langkah 25 (menunggu toast sebelumnya hilang agar toast kedua tidak tertukar, R-12), langkah 31 (mengembalikan checkbox dan menutup popup yang sudah kosong tanpa dialog Unsaved Changes), langkah 34 (baseline jumlah group tree Principal).
- Spec ini sekitar 41 langkah, di atas batas smell sekitar 35. Alasan: seluruh blok satu kelas harness (fungsional Create Group), tiap blok memakai node seed dan nama milik spec sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok yang butuh ganti akun (TC-AC-SG-86) ada di akhir.
- Temuan untuk QA:
  - TC-AC-SG-86 Expected "tree Principal tidak berubah" tidak punya langkah observasi di TC; spec memakai pembacaan jumlah group lewat Fixture BE (kemampuan disediakan tim FE/BE).
  - TC-AC-SG-83 dan TC-AC-SG-89 menyebut nama literal (`Region Trim`, `Region Baru 1`); spec memakai nama bersuffix (S-12) sehingga asersi nama mengikuti nama bersuffix yang sama.
- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (Create Group: Stay on Form, trim nama, dan nama sama pada parent atau entitas berbeda) pada satu form dan satu harness; tiap blok memakai node milik spec sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Dipertahankan satu spec karena blok berbagi seed parent dan pemulihan baseline yang sama.
