---
id: TC-FA-SU-E2E-078-resilience-transaction-role-assign-gagal-bulk-remove-atomik-gagal-dan-kegagalan
title: "Resilience Transaction Role: Assign Gagal, Bulk Remove Atomik Gagal, dan Kegagalan Penulisan Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-255
  - TC-FA-SU-269
  - TC-FA-SU-276
coverage:
  web: automated
---

# Resilience Transaction Role: Assign Gagal, Bulk Remove Atomik Gagal, dan Kegagalan Penulisan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), Changelog (Pre-setup #27), dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: Transfer × Asset Admin pada Finance & Accounting (TC-FA-SU-255 dan 276); dua baris Transaction Role dengan Role berbeda, Disposal × Staff dan Borrowing & Assignment × Approver, dipilih untuk Bulk Remove (TC-FA-SU-269).
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP Submit Assign dan Bulk Remove Transaction Role di atas backend nyata (kegagalan 5xx dipicu intercept, bagian 6 konvensi); intercept dilepas segera setelah pemicu selesai (S-09). Pemicu kegagalan penulisan log di sisi server untuk TC-FA-SU-276 adalah kemampuan "disediakan tim FE" (TC menyatakan kegagalan itu hanya dapat dipicu di sisi server; tidak ada endpoint yang dikarang). Pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10).
- State global yang diubah: tidak ada perubahan Transaction Role yang tersimpan; pemicu kegagalan penulisan log dipulihkan pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-255: Assign Transaction Role gagal karena server error: toast error, modal tetap terbuka, dan input dipertahankan

1. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Intercept respons Submit Assign Transaction Role menjadi 5xx
3. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu isi Transfer × Asset Admin pada Finance & Accounting
4. Klik `[Submit]`
5. Verifikasi toast "Error, failed to assign Asset Admin."
6. Lepas intercept respons Submit
7. Verifikasi modal tetap terbuka dengan input dipertahankan
8. Verifikasi `[Submit]` Enabled untuk retry
9. Klik `[✕]` pada modal
10. Verifikasi dialog `Unsaved Changes`
11. Klik `[Leave]`
12. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
13. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-269: Bulk Remove gagal atomik: seluruh baris batal dan toast error

14. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
15. Intercept respons Bulk Remove Transaction Role menjadi 5xx
16. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role dan centang dua baris dengan Role berbeda (Disposal × Staff dan Borrowing & Assignment × Approver)
17. Klik `[Bulk Remove]` lalu klik `[Remove]`
18. Verifikasi toast "Error, failed to remove Transaction Role."
19. Lepas intercept respons Bulk Remove
20. Verifikasi baris Disposal × Staff dan Borrowing & Assignment × Approver masih tampil di tabel (tidak ada baris yang terhapus)
21. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
22. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-276: Kegagalan penulisan log Transaction Role membatalkan perubahan karena atomik dengan aksi utama

23. Picu kegagalan penulisan log di sisi server (kemampuan disediakan tim FE)
24. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu isi Transfer × Asset Admin pada Finance & Accounting dan klik `[Submit]`
25. Verifikasi toast error tampil
26. Verifikasi tidak ada baris baru Transfer × Asset Admin di tabel
27. Pulihkan layanan penulisan log di sisi server

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 6, 9 sampai 11, 14, 19, 23 dan 27. Intercept dilepas segera setelah toast error tampil (S-09); penutupan modal dirty mengikuti S-08; baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 12, 13, 21 dan 22. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Klausa "tidak ada entri log" pada TC-FA-SU-255 dan 269 (aksi yang gagal) ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); toast error menjadi anchor positif.
- `K-1`: TC-FA-SU-276 berkolom FE Test `-` (PIC BE) dan Automation `Manual Only — BE`; TC itu tetap menjadi sumber spec FE+BE karena tidak ada `tc-settings-user-backend.md` dan Expected-nya (toast error dan tabel tanpa baris baru) dapat diamati di UI. Pemicu kegagalan penulisan log adalah kemampuan "disediakan tim FE" tanpa asersi atas kegagalan yang dipicu UI.
- Temuan untuk QA:
  - TC-FA-SU-276 butir a ("toast error tampil") tidak menyebut teks toast; spec hanya mengasersi toast error tampil. TC-FA-SU-276 tidak menyebut Pre-setup #27 (Changelog) pada Expected; tidak ada asersi log.
  - TC-FA-SU-269 butir a menyebut "atau memuat nama Role bila sama" untuk toast; spec memakai dua baris dengan Role berbeda sehingga toast "Error, failed to remove Transaction Role."
  - Post Condition TC-FA-SU-255, 269, dan 276 sudah tercakup oleh Expected di atas.
