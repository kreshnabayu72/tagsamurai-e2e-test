---
id: TC-FA-SU-E2E-081-popup-assign-group-cancel-dialog-d-06-d-07-dan-node-disabled-already-assigned
title: "Popup Assign Group: Cancel Dialog D-06 D-07 dan Node Disabled Already Assigned"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-263
  - TC-FA-SU-264
coverage:
  web: automated
---

# Popup Assign Group: Cancel Dialog D-06 D-07 dan Node Disabled Already Assigned

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable, IT Infrastructure, Branch Surabaya, dan grup lain) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; baris Disposal × Staff pada Finance & Accounting.
- Data uji: Finance & Accounting dicabut dan IT Infrastructure ditambahkan lalu dibatalkan di dialog (TC-FA-SU-263); Search `Surabaya` pada popup (TC-FA-SU-264).
- Kemampuan teknis: pembacaan state data Transaction Role Mira Anggraini lewat fixture BE dan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: tidak ada penugasan yang tersimpan; perubahan popup dibuang.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-263: Assign Group: Cancel pada dialog D-06 atau D-07 membatalkan seluruh Save

1. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
3. Hapus centang Finance & Accounting dan centang IT Infrastructure
4. Klik `[Save]`
5. Klik `[Cancel]` pada dialog
6. Verifikasi seluruh Save dibatalkan: Disposal × Staff Mira Anggraini tetap memuat Finance & Accounting saja (state data lewat fixture BE)
7. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
8. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-264: Assign Group tidak menampilkan node Disabled already assigned dan tanpa cascade

9. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
10. Verifikasi node Finance & Accounting yang ter-assign tercentang dan dapat dicabut centangnya (bukan Disabled)
11. Hapus centang lalu centang kembali Finance & Accounting dan amati Accounts Payable
12. Verifikasi mencentang parent tidak mencentang child: Accounts Payable tidak tercentang
13. Cari `Surabaya` pada Search popup
14. Verifikasi node Branch Surabaya tampil
15. Verifikasi node yang tidak cocok dengan `Surabaya` (IT Infrastructure) tidak tampil
16. Kosongkan Search popup lalu klik `[✕]` pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1 dan 16. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 7 dan 8. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-263: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); state data Disposal × Staff yang tidak berubah menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-SU-263 menyebut "dialog D-06 atau D-07" tetapi perubahan yang diberikan (cabut Finance & Accounting, tambah IT Infrastructure) memicu hanya dialog pencabutan D-07 (Role baris tidak berubah); dialog D-06 tidak teruji pada TC ini. TC juga tidak menyebut keadaan popup sesudah `[Cancel]`; spec mengasersi state data lewat fixture BE.
  - TC-FA-SU-264 langkah 3 ("Centang Finance & Accounting") tidak mungkin dilakukan karena Finance & Accounting sudah ter-assign dan tercentang; spec menghapus centang lalu mencentang kembali sebelum mengamati Accounts Payable. TC-FA-SU-264 butir c ("Search memfilter node yang tampil") tidak menyebut node mana yang harus tampil; spec memakai Branch Surabaya (cocok `Surabaya`) dan IT Infrastructure (tidak cocok).
