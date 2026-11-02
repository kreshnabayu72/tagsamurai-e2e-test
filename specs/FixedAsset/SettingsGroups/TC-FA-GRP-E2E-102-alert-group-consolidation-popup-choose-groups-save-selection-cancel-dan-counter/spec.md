---
id: TC-FA-GRP-E2E-102-alert-group-consolidation-popup-choose-groups-save-selection-cancel-dan-counter
title: "Alert Group Consolidation: [Choose Groups] Membuka Popup Konten Step, [Save Selection] Diterapkan Seketika, dan Counter dengan Batas Cap dan Minimal 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1110
  - TC-FA-GRP-1111
  - TC-FA-GRP-1117
coverage:
  web: automated
---

# Alert Group Consolidation: [Choose Groups] Membuka Popup Konten Step, [Save Selection] Diterapkan Seketika, dan Counter dengan Batas Cap dan Minimal 1

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client khusus Group Consolidation (Pre-setup No 25, bukan client Tabel A; plan Growth; client punya tepat 5 group dengan status Excess sesuai blok; email dan `Spectra.env.FA_ALERT_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed ulang oleh fixture BE di `before`): cap plan berlaku 3, client khusus Group Consolidation (Pre-setup No 25) punya tepat 5 group: `E1` dan `E2` berstatus Excess, `U1`, `U2`, dan `U3` usable (data untuk TC-1111 dan juga dipakai TC-1110 dan TC-1117).
- State tenant (kelas h): cap plan dan status Excess diatur per blok oleh fixture BE (disediakan tim FE/BE); plan, cap, dan status Excess dipulihkan di hook `after`. Suite berjalan serial.
- Cleanup di `after`: hapus group seed dan pulihkan keadaan lewat fixture BE.

## Test Steps

### TC-FA-GRP-1110: [Choose Groups] membuka popup dan [Cancel] menutup tanpa perubahan

1. Klik [Choose Groups]
2. Verifikasi popup Group Consolidation terbuka dengan header "Choose which groups stay active"
3. Verifikasi tabel popup memuat kolom Keep usable, Group, Total Asset, dan Total User
4. Verifikasi counter `[Selected Groups] of [Group Limit] selected`
5. Verifikasi footer memuat [Cancel] dan [Save Selection]
6. Verifikasi seluruh checkbox unchecked saat popup dibuka
7. Klik [Cancel] tanpa mengubah centang
8. Verifikasi popup tertutup tanpa dialog Unsaved changes
9. Verifikasi status Excess tidak berubah (`E1` dan `E2` tetap Excess)

### TC-FA-GRP-1117: Counter dan [Save Selection] mengikuti batas cap dan minimal 1

10. Klik [Choose Groups]
11. Verifikasi [Save Selection] disabled
12. Verifikasi counter "0 of 3 selected" netral
13. Centang 3 group
14. Verifikasi [Save Selection] enabled
15. Verifikasi counter "3 of 3 selected"
16. Centang group ke-4
17. Verifikasi [Save Selection] disabled
18. Verifikasi counter "4 of 3 selected" dengan severity danger
19. Uncheck group ke-4
20. Verifikasi [Save Selection] enabled kembali
21. Uncheck ketiga group yang tercentang (kembali ke keadaan saat popup dibuka: 0 tercentang)
22. Klik [Cancel]
23. Verifikasi popup langsung tertutup tanpa dialog Unsaved changes

### TC-FA-GRP-1111: [Save Selection] diterapkan seketika dan Alert tetap tampil

24. Klik [Choose Groups]
25. Centang `E1`, `U1`, dan `U2` (`E2` dan `U3` tidak dicentang)
26. Klik [Save Selection]
27. Verifikasi toast "Success, group consolidation has been updated."
28. Verifikasi popup tertutup
29. Verifikasi `E1` kembali usable, `U1` dan `U2` tetap usable, `E2` tetap Excess, dan `U3` berubah Excess (nama di-dim)
30. Verifikasi total usable 3 dan Excess 2
31. Verifikasi Alert Group Consolidation tetap tampil karena jumlah group masih 5 di atas cap 3

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 21, 22: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Penutupan popup pada TC-1117 (langkah 21 sampai 23) mengembalikan centang ke keadaan saat popup dibuka (net-zero) sehingga popup langsung tertutup tanpa dialog.
- TC-1111 terakhir karena mengubah status Excess; keadaan awal dipulihkan oleh fixture BE di `after`.
- Temuan untuk QA:
  - TC-1110 memakai placeholder `[Selected Groups]` dan `[Group Limit]` pada counter; spec mengasersi counter pada format yang sama, nilai konkret diasersi pada TC-1117.
  - TC-1110 Precondition tidak menyebut client dan akun; disediakan tim FE.
