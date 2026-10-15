---
id: TC-AC-PP-E2E-052-sesi-pengguna-lain-tidak-terganggu
title: "Publish Tidak Mengganggu Sesi Pengguna Lain dan Tidak Mengirim Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-165
coverage:
  web: automated
---

# Publish Tidak Mengganggu Sesi Pengguna Lain dan Tidak Mengirim Notifikasi

## Prerequisites

- Mode: FE+BE.
- Dua konteks browser berjalan bersamaan (kelas harness c, multi-konteks).

| Konteks | Peran | Nama tampil | Email | Env var password |
|---|---|---|---|---|
| 1 (aktor Publish) | Total Control (Pre-setup 1) | `Andi Wijaya` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| 2 (pengguna lain, sesi aktif) | Client User (Pre-setup 8) | `Budi Aditya` | `budiaditya@qwertysystem.net` | `Spectra.env.AC_BUDI_PASSWORD` |

- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1) dan memastikan `Budi Aditya` sudah menyetujui Version 3 (persetujuan Privacy Policy versi 3 tercatat); login konteks 1 sebagai Total Control (aktor pertama). Login `Budi Aditya` di konteks 2 dilakukan di hook `before` yang sama (sesi aktif sebelum langkah pertama), karena spec harus dimulai dengan sesi lain yang sudah berjalan.
- Hook `after` (tetap jalan walau spec gagal): logout konteks 2, mengembalikan dataset ke Riwayat A, dan mengembalikan sesi konteks 1 ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Kemampuan teknis: dua konteks browser paralel dengan sesi login berbeda; Fixture BE (seeding Riwayat A dan persetujuan `Budi Aditya`); akses ke Notification Center aplikasi Client User; mail-catcher lingkungan uji yang dapat dibaca per alamat `budiaditya@qwertysystem.net` untuk mengamati email. Nama env `AC_BUDI_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`, belum terdaftar (`AC_TC_PASSWORD` sudah terdaftar).
- Baseline (S-12): jumlah notifikasi di Notification Center `Budi Aditya` dan jumlah email di mail-catcher `budiaditya@qwertysystem.net` dicatat sebelum Publish; asersi memakai selisih terhadap baseline.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish `Version 4`, sehingga suite berjalan serial (`parallel: false`) dan dataset dipulihkan ke Riwayat A di hook `after`.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Langkah 3 |

## Test Steps

### TC-AC-PP-165: Publish tidak mengganggu sesi pengguna lain yang sedang aktif dan tidak mengirim notifikasi

1. Pada konteks 2 (sesi `Budi Aditya`), buka Notification Center dan catat jumlah notifikasi sebagai baseline notifikasi
2. Pada konteks 2, buka mail-catcher untuk `budiaditya@qwertysystem.net` dan catat jumlah email sebagai baseline email
3. Pada konteks 1 (Total Control, `Andi Wijaya`), buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
4. Pada konteks 1, klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
5. Pada konteks 1, klik di akhir konten editor lalu ketik " Forward only."
6. Pada konteks 1, klik `[Publish New Version]`
7. Pada konteks 1, klik `[Publish]` pada Dialog Publish Confirm sehingga `Version 4` terbentuk
8. Pada konteks 2 (sesi `Budi Aditya`), lanjutkan menggunakan aplikasi dengan berpindah menu tanpa logout
9. Verifikasi sesi `Budi Aditya` tetap aktif
10. Verifikasi tidak ada logout paksa pada sesi `Budi Aditya`
11. Verifikasi tidak ada layar Confirm to Continue yang muncul di tengah sesi `Budi Aditya`
12. Pada konteks 2, buka Notification Center `Budi Aditya`
13. Verifikasi jumlah notifikasi sama dengan baseline notifikasi (tidak ada notifikasi baru terkait Privacy Policy)
14. Pada konteks 2, buka mail-catcher untuk `budiaditya@qwertysystem.net`
15. Verifikasi jumlah email sama dengan baseline email (tidak ada email baru)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness c (multi-konteks): dua sesi paralel dalam satu skenario. Kolom Automation TC bernilai "Manual Only — (d) dua sesi pengguna paralel dalam satu skenario"; sesuai konvensi bagian 2 hambatan teknis bukan alasan mengeluarkan TC, sehingga kebutuhan dua konteks ditulis di Prerequisites untuk tim FE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 1 dan 2 (pencatatan baseline) serta langkah 14 (buka mail-catcher untuk mengamati email) adalah pencatatan dan pembukaan layar tanpa asersi sendiri.
- Asersi atas TC: langkah 13 dan 15 memakai baseline (S-12) karena TC menyatakan "tidak ada notifikasi baru" dan "tidak ada email"; baseline ditambahkan agar asersi berarti walau Notification Center atau mail-catcher sudah berisi data lama.
- Expected c TC-165 ("tidak ada email atau notifikasi proaktif lain") dipecah per klausa (S-01): "email" diasersi di langkah 15, "notifikasi proaktif lain" dicakup langkah 13 (jumlah notifikasi sama dengan baseline).
- Temuan untuk QA:
  - TC tidak menyebut cara `Budi Aditya` menyetujui Version 3 (precondition b) maupun cara mengamati "email atau notifikasi proaktif lain" (Expected c). Spec memakai Fixture BE untuk persetujuan dan mail-catcher untuk email; mekanisme ini bukan dari TC dan perlu dikonfirmasi tim FE/QA.
  - Post Condition TC ("sesi `Budi Aditya` tidak berubah") tidak punya langkah observasi di luar Expected a dan tidak diasersi tambahan.
