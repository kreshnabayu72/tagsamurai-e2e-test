---
id: TC-AC-SU-E2E-041-bulk-resend-sukses-cooldown-dan-semua-cooldown
title: "Bulk Resend Activation Email: Sukses, Sebagian Cooldown, dan Semua Cooldown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-154
  - TC-AC-SU-156
  - TC-AC-SU-157
coverage:
  web: automated
---

# Bulk Resend Activation Email: Sukses, Sebagian Cooldown, dan Semua Cooldown

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (Pending Activation, seed lewat Fixture BE): `Mike Tan {runId}-041`, `Sarah Lee {runId}-041` (TC-154 dan TC-157), `Rudi Hartono {runId}-041`, `Dedi Kurnia {runId}-041` (TC-156).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-041@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-041`.
- Jam server dan jam browser dibekukan di langkah awal supaya cooldown 60 detik tidak berakhir selama spec (bagian 6; R-10); dipulihkan di langkah penghubung terakhir dan di hook `after`. Kemampuan bekukan jam disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku yang hanya memicu perubahan state (suite.md); disediakan tim BE/FE.
- Data milik spec (user) di-seed hook `before` dengan suffix `{runId}-041` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-154: Bulk Resend Activation Email: semua baris Pending Activation

1. Bekukan jam server dan jam browser pada waktu nyata saat ini
2. Ketik Search `{runId}-041`, tekan Enter
3. Centang `Mike Tan {runId}-041`, `Sarah Lee {runId}-041` (Pending Activation, tidak dalam cooldown)
4. Klik `[Bulk Action ▾]` lalu `Resend Activation Email`
5. Verifikasi muncul toast sukses: "Success, email has been sent."
6. Verifikasi seleksi di-reset: checkbox `Mike Tan {runId}-041` dan `Sarah Lee {runId}-041` tidak tercentang
7. Tunggu toast lama hilang otomatis

### TC-AC-SU-156: Bulk Resend: baris dalam cooldown dihitung skipped

8. Pemicu (sesi API aktor Total Control): kirim Resend Activation Email untuk `Rudi Hartono {runId}-041` hingga cooldown tersimpan
9. Centang `Rudi Hartono {runId}-041` (dalam cooldown) dan `Dedi Kurnia {runId}-041` (tidak dalam cooldown)
10. Klik `[Bulk Action ▾]` lalu `Resend Activation Email`
11. Verifikasi muncul toast sukses: "Success, email has been sent. Some items were skipped."
12. Verifikasi seleksi di-reset: checkbox `Rudi Hartono {runId}-041` dan `Dedi Kurnia {runId}-041` tidak tercentang
13. Tunggu toast lama hilang otomatis

### TC-AC-SU-157: Bulk Resend: semua baris dalam cooldown (0 berhasil)

14. Catat jumlah baris tampil pada User List
15. Centang `Mike Tan {runId}-041` dan `Sarah Lee {runId}-041` (keduanya dalam cooldown dari TC-154)
16. Klik `[Bulk Action ▾]` lalu `Resend Activation Email`
17. Verifikasi muncul toast error: "Error, failed to send email. Please wait a moment before resending."
18. Verifikasi list tidak berubah: jumlah baris sama dengan yang dicatat sebelum Resend
19. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 2, 7, 8, 13, 19 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah 14 (catat jumlah baris tampil) adalah langkah penghubung tambahan (S-03, dasar 8b.2) sebagai pembanding bagi Verifikasi langkah 18.
- TC-157 memakai `Mike Tan {runId}-041` dan `Sarah Lee {runId}-041` yang masuk cooldown oleh TC-154 (jam dibekukan sehingga tetap dalam cooldown); TC-156 memakai dua user lain agar satu dalam cooldown dan satu tidak.
- Temuan untuk QA:
  - Post Condition TC-154, 156, 157 ("email terkirim", "entri log", "Email hanya ke `Sarah Lee`") tidak punya langkah observasi dan tidak diasersi.
  - "List tidak berubah" (TC-157) tidak merinci; spec mengasersi jumlah baris yang sama.
  - TC-156 tidak menyatakan cara membuat cooldown; spec memakai sesi API Total Control sebagai pemicu.
