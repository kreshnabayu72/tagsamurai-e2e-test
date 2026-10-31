---
id: TC-GS-GSET-E2E-018-dialog-unsaved-changes-cancel-leave-esc-dan-backdrop
title: "Dialog Unsaved Changes: Cancel, Leave, Esc, dan Klik Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-49
  - TC-GS-GSET-50
  - TC-GS-GSET-116
coverage:
  web: automated
---

# Dialog Unsaved Changes: Cancel, Leave, Esc, dan Klik Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`). Spec ini tidak pernah menyimpan perubahan, sehingga record tidak berubah.
- Kemampuan teknis: menekan `Tab` berulang kali dan membaca elemen yang berfokus (fokus terjebak di dalam dialog).
- Data Uji: Session Idle Timeout `1 hour`; tujuan navigasi in-app Global Settings > Activity Log (klik menu pada sidebar). Tidak ada Data Dinamis dan tidak ada baris Changelog yang dihasilkan.
- TC-GS-GSET-49, 50, 116: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-49, TC-GS-GSET-116, dan TC-GS-GSET-50: Dialog Unsaved Changes muncul; backdrop dan Esc

1. Pilih Session Idle Timeout `1 hour`
2. Klik menu Global Settings > Activity Log pada sidebar
3. Verifikasi Dialog Unsaved Changes muncul dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
4. Tekan `Tab` berulang kali
5. Verifikasi fokus keyboard terjebak di dalam dialog selama dialog terbuka
6. Klik area backdrop di luar dialog
7. Verifikasi Dialog Unsaved Changes tetap terbuka
8. Verifikasi masih berada di General Settings
9. Tekan `Esc`
10. Verifikasi dialog tertutup
11. Verifikasi tetap berada di General Settings
12. Verifikasi Session Idle Timeout tetap `1 hour`

### TC-GS-GSET-49: Cancel lalu Leave

13. Klik menu Global Settings > Activity Log pada sidebar
14. Klik `[Cancel]`
15. Verifikasi dialog tertutup
16. Verifikasi tetap berada di General Settings
17. Verifikasi Session Idle Timeout tetap `1 hour`
18. Klik menu Global Settings > Activity Log pada sidebar
19. Klik `[Leave]`
20. Verifikasi pindah ke Activity Log tanpa menyimpan (halaman Activity Log tampil)
21. Klik menu Global Settings > General Settings pada sidebar
22. Verifikasi Session Idle Timeout `30 minutes` (perubahan tidak tersimpan)

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional (satu topik: Dialog Unsaved Changes pada navigasi in-app).
- Urutan TC di spec berbeda dari urutan sumber (49, 116, 50 sebelum Cancel dan Leave dari TC-GS-GSET-49): dialog yang dibuka sekali pada langkah 2 dipakai untuk TC-GS-GSET-116 (backdrop) dan TC-GS-GSET-50 (`Esc`) sebelum Cancel dan Leave, sehingga `[Leave]` (aksi yang membuang perubahan) ditaruh paling akhir (bagian 3 prinsip 5, S-10). Keadaan sebelum tiap TC sama dengan precondition TC (perubahan Session Idle Timeout `1 hour` belum tersimpan, dialog muncul dari klik menu Activity Log).
- Pemetaan Expected: TC-GS-GSET-49 a ke langkah 3, b ke 15 sampai 17, c ke 20, d ke 22; TC-GS-GSET-50 a ke langkah 10 sampai 12, b ke 5; TC-GS-GSET-116 ke langkah 7 dan 8.
- Langkah 4 (menekan `Tab`) adalah pemicu pengamatan fokus terjebak TC-GS-GSET-50; fokus diasersi sebelum `Esc` menutup dialog (bagian 8b butir 5).
- Langkah 13 dan 18 membuka kembali dialog lewat klik menu yang sama (langkah 2 dan 5 TC-GS-GSET-49); langkah 21 adalah langkah 7 TC-GS-GSET-49 (kembali ke General Settings). Tidak ada langkah penghubung lain.
- Temuan untuk QA:
  - TC-GS-GSET-49: Expected a hanya menyebut teks isi dialog dan dua tombol; PRD tidak menyebut judul Dialog Unsaved Changes, sehingga spec tidak mengasersi judul.
