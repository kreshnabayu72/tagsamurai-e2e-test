---
id: TC-AC-SU-E2E-176-resilience-activate-deactivate-dan-bulk-gagal-server
title: "Resilience Activate, Deactivate, dan Bulk Activate atau Deactivate Gagal Server (5xx atau Timeout) Mengembalikan Switch dan Menampilkan Toast Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-92
  - TC-AC-SU-93
  - TC-AC-SU-130
  - TC-AC-SU-131
  - TC-AC-SU-132
coverage:
  web: automated
---

# Resilience Activate, Deactivate, dan Bulk Activate atau Deactivate Gagal Server (5xx atau Timeout) Mengembalikan Switch dan Menampilkan Toast Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu set user bersama (kegagalan server tidak mengubah status, sehingga user tidak berubah antar blok; nama berprefix `{runId}-176`):

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `John Doe {runId}-176A` | `johndoe+{runId}-176a@qwertysystem.net` | Activated, Active |
| B | `Rina Putri {runId}-176B` | `rinaputri+{runId}-176b@qwertysystem.net` | Activated, Active |
| C | `Jane Smith {runId}-176C` | `janesmith+{runId}-176c@qwertysystem.net` | Activated, Inactive |
| D | `Budi Santoso {runId}-176D` | `budisantoso+{runId}-176d@qwertysystem.net` | Activated, Inactive |

- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP request Deactivate, Activate, Bulk Deactivate, dan Bulk Activate (500 atau timeout tanpa respons); endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec. Spec memakai backend nyata dengan intercept parsial (bukan `Mode: mock`) karena status user diasersi dari state nyata. Intercept dilepas segera setelah toast error diasersi (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-92: Deactivate gagal server (5xx)
1. Atur intercept: respons request Deactivate dikembalikan 500
2. Ketik Search `John Doe {runId}-176A`, tekan Enter, lalu klik switch Active baris A
3. Klik `[Deactivate]`
4. Verifikasi toast error `"Error, failed to deactivate user."`
5. Verifikasi switch Active baris A rollback ke ON
### TC-AC-SU-93: Activate gagal karena timeout
6. Lepas intercept sebelumnya, lalu atur intercept: respons request Activate tidak dijawab sampai timeout
7. Ketik Search `Jane Smith {runId}-176C`, tekan Enter, lalu klik switch Active baris C
8. Klik `[Activate]`
9. Verifikasi toast error `"Error, failed to activate user."`
10. Verifikasi switch Active baris C rollback ke OFF
### TC-AC-SU-130: Bulk Deactivate gagal menyeluruh di server
11. Lepas intercept sebelumnya, atur intercept: respons request Bulk Deactivate dikembalikan 5xx, lalu tunggu toast error lama hilang otomatis
12. Ketik Search `{runId}-176`, tekan Enter, lalu centang baris A dan baris B
13. Klik `[Bulk Action ▾]`, lalu pilih `Deactivate`
14. Klik `[Deactivate]` pada dialog
15. Verifikasi toast error `"Error, failed to deactivate user."`
16. Verifikasi toast `"Error, failed to send email. Please wait a moment before resending."` tidak tampil
17. Verifikasi switch Active baris A dan baris B tetap ON
### TC-AC-SU-131: Bulk Deactivate gagal menyeluruh (5xx atau timeout)
18. Tunggu toast error lama hilang otomatis, klik icon `×` pada Bulk Action Bar, centang baris A dan baris B, lalu klik `[Bulk Action ▾]` dan pilih `Deactivate`
19. Klik `[Deactivate]` pada dialog
20. Verifikasi toast error `"Error, failed to deactivate user."`
21. Verifikasi status baris A dan baris B tidak berubah (tetap Active)
### TC-AC-SU-132: Bulk Activate gagal menyeluruh (5xx)
22. Lepas intercept sebelumnya, atur intercept: respons request Bulk Activate dikembalikan 5xx, lalu tunggu toast error lama hilang otomatis
23. Klik icon `×` pada Bulk Action Bar, centang baris C dan baris D
24. Klik `[Bulk Action ▾]`, lalu pilih `Activate`
25. Klik `[Activate]` pada dialog
26. Verifikasi toast error `"Error, failed to activate user."`
27. Lepas intercept, lalu klik icon `×` pada Bulk Action Bar

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search untuk menemukan baris target (R-16), klik icon `×` pada Bulk Action Bar untuk melepas seleksi parsial (S-09; `Unselect All` hanya tampil setelah Select All), dan menunggu toast error lama hilang sebelum menghitung toast berikutnya (R-12). Seleksi dilepas sebelum tiap blok bulk berikutnya.
- Kegagalan server hanya mengamati perilaku UI atas respons gagal; Post Condition TC-92 ("Status tetap Active; tidak ada entri log"), TC-93, TC-130 (tidak ada entri di Changelog: User, System Log, Activity Log), dan TC-132 tidak punya langkah observasi di TC dan tidak diasersi di spec ini.
- Lima blok TC kelas b berpola sama (intercept, aksi, toast error, rollback) dan berdiri sendiri pada user seeding yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-92 dan TC-93 menyebut "Response ... disimulasikan 500/timeout" tanpa menyebut endpoint; spec memakai intercept pada request aksi terkait tanpa menyebut path.
  - TC-130 dan TC-131 memiliki langkah dan Expected hampir identik (Bulk Deactivate 5xx); TC-131 menyebut "5xx/timeout" sedangkan spec memakai 5xx yang sama dengan TC-130 (timeout hanya pada TC-93).
  - TC-132 memuat Post Condition "status baris C dan D tidak berubah (tetap Inactive)" tanpa langkah observasi di TC; spec tidak mengasersinya.
  - TC-131 dan TC-132 tidak menyebut precondition user yang dipakai; spec memakai user seeding bersuffix.
