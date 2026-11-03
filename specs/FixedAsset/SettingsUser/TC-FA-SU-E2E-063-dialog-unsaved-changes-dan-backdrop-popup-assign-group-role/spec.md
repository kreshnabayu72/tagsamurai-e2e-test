---
id: TC-FA-SU-E2E-063-dialog-unsaved-changes-dan-backdrop-popup-assign-group-role
title: "Dialog Unsaved Changes dan Backdrop Popup Assign Group Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-207
  - TC-FA-SU-208
coverage:
  web: automated
---

# Dialog Unsaved Changes dan Backdrop Popup Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya.
- Data uji: perubahan yang diuji adalah mencentang Delete pada baris Branch Surabaya (TC-FA-SU-207 dan 208).
- State global yang diubah: tidak ada penugasan yang disimpan; semua perubahan popup dibuang lewat `[Leave]`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-207: Dialog Unsaved Changes saat menutup popup dengan perubahan: copy, Leave, dan Cancel

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
2. Centang Delete pada Branch Surabaya lalu klik `[✕]`
3. Verifikasi dialog dengan Body "You have unsaved changes. Are you sure you want to leave?" tanpa bullet
4. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Leave]` (filled danger)
5. Klik `[Cancel]`
6. Verifikasi popup kembali tampil dengan isi dipertahankan (Delete Branch Surabaya tercentang)
7. Klik `[✕]` lagi lalu klik `[Leave]`
8. Verifikasi popup menutup
9. Buka ulang popup Assign Group Role Manage files
10. Verifikasi Delete Branch Surabaya tidak tercentang (perubahan dibuang)
11. Centang Delete pada Branch Surabaya, hapus centang Delete, lalu klik `[✕]`
12. Verifikasi popup langsung menutup tanpa dialog (perubahan dikembalikan persis ke nilai awal bukan dirty)

### TC-FA-SU-208: Popup Assign Group Role tanpa perubahan menutup langsung dan klik backdrop tidak menutup popup

13. Buka popup Assign Group Role Manage files
14. Klik `[✕]`
15. Verifikasi popup menutup langsung tanpa dialog
16. Buka ulang popup Assign Group Role Manage files lalu klik backdrop
17. Verifikasi popup tidak menutup
18. Verifikasi tidak ada dialog yang muncul
19. Centang Delete pada Branch Surabaya lalu tekan Esc
20. Verifikasi dialog `Unsaved Changes` tampil
21. Klik `[Leave]` untuk membuang perubahan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 21; `[Leave]` menutup popup dirty (S-08).
- TC-FA-SU-209 dan 210 (popup yang sama dengan pelaku kedua lewat sesi API) ada di spec 087.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-207 dan 208 ("penugasan tersimpan tidak berubah dan tidak ada entri log") tidak punya langkah observasi di TC dan tidak diasersi.
