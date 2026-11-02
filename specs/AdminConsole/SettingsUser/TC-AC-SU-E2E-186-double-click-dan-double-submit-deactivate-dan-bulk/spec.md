---
id: TC-AC-SU-E2E-186-double-click-dan-double-submit-deactivate-dan-bulk
title: "Double-Click dan Double-Submit pada Dialog Deactivate, Bulk Deactivate, dan Bulk Activate Hanya Memproses Satu Request"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-103
  - TC-AC-SU-135
  - TC-AC-SU-628
  - TC-AC-SU-629
coverage:
  web: automated
---

# Double-Click dan Double-Submit pada Dialog Deactivate, Bulk Deactivate, dan Bulk Activate Hanya Memproses Satu Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec (nama berprefix `{runId}-186`):

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `John Doe {runId}-186A` | `johndoe+{runId}-186a@qwertysystem.net` | Activated, Active (TC-103) |
| B | `Rina Putri {runId}-186B` | `rinaputri+{runId}-186b@qwertysystem.net` | Activated, Active (TC-135) |
| C | `Budi Santoso {runId}-186C` | `budisantoso+{runId}-186c@qwertysystem.net` | Activated, Active (TC-135) |
| D | `John Doe {runId}-186D` | `johndoe+{runId}-186d@qwertysystem.net` | Activated, Active (TC-628) |
| E | `Jane Smith {runId}-186E` | `janesmith+{runId}-186e@qwertysystem.net` | Activated, Inactive (TC-629) |
| F | `Mike Tan {runId}-186F` | `miketan+{runId}-186f@qwertysystem.net` | Activated, Inactive (TC-629) |

- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Deactivate, Bulk Deactivate, dan Bulk Activate sampai dilepas (penahanan hanya untuk mengamati state Loading; bukan kegagalan, sehingga bukan kelas b) dan untuk menghitung jumlah request yang terkirim; Fixture BE. Tahanan dilepas segera sesudah asersi Loading (S-09). Tanpa jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-103: Double-click [Deactivate] pada satu user
1. Tunggu toast lama hilang otomatis, ketik Search `John Doe {runId}-186A`, tekan Enter, lalu klik switch Active baris A
2. Tahan respons request Deactivate, lalu klik `[Deactivate]` dua kali secepatnya
3. Verifikasi tombol `[Deactivate]` masuk state loading atau disabled setelah klik pertama
4. Lepas tahanan respons
5. Verifikasi hanya 1 toast sukses `"Success, user has been deactivated."`
### TC-AC-SU-135: Double-click [Deactivate] pada dialog bulk
6. Tunggu toast sukses lama hilang otomatis, ganti isi kotak search dengan `{runId}-186`, tekan Enter, lalu centang baris B dan baris C
7. Klik `[Bulk Action ▾]`, lalu pilih `Deactivate`
8. Tahan respons request Bulk Deactivate, lalu klik `[Deactivate]` pada dialog dua kali secepatnya
9. Verifikasi tombol `[Deactivate]` masuk state loading atau disabled setelah klik pertama
10. Lepas tahanan respons
11. Verifikasi tepat 1 toast sukses
### TC-AC-SU-628: Double-submit dialog Deactivate hanya 1 entri log
12. Tunggu toast sukses lama hilang otomatis, lalu klik switch Active baris D (`John Doe {runId}-186D`)
13. Tahan respons request Deactivate, lalu klik `[Deactivate]` dua kali secepatnya
14. Verifikasi tombol `[Deactivate]` masuk state loading atau disabled setelah klik pertama
15. Lepas tahanan respons
16. Tunggu aksi selesai
17. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
18. Ketik Search `John Doe {runId}-186D` pada Popup Changelog: User, tekan Enter
19. Verifikasi hanya 1 entri log baru untuk D (Action `Deactivate`)
### TC-AC-SU-629: Double-submit Bulk Activate hanya 1 entri log
20. Tutup popup, ganti isi kotak search dengan `{runId}-186`, tekan Enter, lalu centang baris E dan baris F
21. Klik `[Bulk Action ▾]`, lalu pilih `Activate`
22. Tahan respons request Bulk Activate, lalu klik `[Activate]` pada dialog dua kali secepatnya
23. Verifikasi tombol `[Activate]` masuk state loading atau disabled setelah klik pertama
24. Lepas tahanan respons
25. Tunggu aksi selesai
26. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
27. Ketik Search `{runId}-186` pada Popup Changelog: User, tekan Enter
28. Verifikasi masing-masing E dan F hanya memiliki 1 entri log baru (Action `Activate`)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), menunggu toast lama hilang (R-12), menahan dan melepas respons, serta menunggu aksi selesai sesudah tahanan dilepas dan sebelum membuka Popup Changelog: User (8b.8). Asersi state Loading ditulis sebelum tahanan dilepas (bagian 8b butir 5). User bernama unik sehingga baseline entri nol dan "1 entri log baru" menjadi asersi jumlah (bukan absence kelas g).
- TC-AC-SU-103 dan TC-AC-SU-628 adalah pasangan topik yang sama dengan sudut berbeda (toast dan entri log); keduanya tetap di spec ini sebagai blok terpisah dengan user seeding berbeda. Post Condition TC-103 ("Tepat 1 entri log Deactivate") dan TC-135 ("Tepat 1 entri log per user") tidak punya langkah observasi di TC dan tidak diasersi.
- Empat blok berpola sama (satu aksi diklik dua kali, state loading, hasil tunggal) dan berdiri sendiri pada user seeding sendiri; 28 langkah wajar.
- Temuan untuk QA:
  - TC-103 dan TC-135 tidak menyebut cara menahan respons untuk mengamati state loading; spec memakai penahanan respons lewat intercept. TC-135 dan TC-629 tidak menyebut jumlah user pada seleksi; spec memakai dua baris.
  - TC-135 butir b ("Tepat 1 toast sukses") tidak menyebut teks toast bulk; spec mengasersi jumlah tanpa teks. TC-629 butir b ("Hanya 1 entri log baru") tidak menyebut apakah per request atau per user; spec mengasersi satu entri per user.
  - TC-628 dan TC-629 menyebut "Buka surface terkait" tanpa menyebut surface; spec memakai dialog Deactivate dan dialog Bulk Activate pada Settings > User.
  - TC memakai nama literal (`John Doe`, `Jane Smith`, `Rina Putri`); spec memakai nama bersuffix (S-12).
