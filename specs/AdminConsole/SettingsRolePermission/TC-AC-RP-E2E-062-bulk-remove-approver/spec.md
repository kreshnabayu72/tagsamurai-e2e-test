---
id: TC-AC-RP-E2E-062-bulk-remove-approver
title: "Bulk Remove Approver: Banyak Baris, Satu Baris Memakai Dialog Single, dan Partial Success"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-211
  - TC-AC-RP-212
  - TC-AC-RP-213
coverage:
  web: automated
---

# Bulk Remove Approver: Banyak Baris, Satu Baris Memakai Dialog Single, dan Partial Success

## Prerequisites

- Mode: FE+BE (intercept respons di atas backend nyata untuk TC-AC-RP-213).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa`), #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`).
- Data Dinamis: spec ini tidak membuat Data Dinamis; target Remove adalah approver Pre-setup. Nilai bersuffix `+{runId}-062` tidak dipakai karena tidak ada data yang dibuat spec.
- Kemampuan teknis (Pre-setup #23): intercept respons jaringan untuk penolakan per baris pada baris `Dewi Anggraini` (TC-AC-RP-213); intercept dilepas segera setelah pemicu selesai.
- Perubahan Pre-setup: approver `Manage allocation` `Region Jawa` dihapus pada TC-AC-RP-211 dan TC-AC-RP-213. Pemulihan memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Role Detail menerima entri Remove; Last Updated approver berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-211: Bulk Remove Approver

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Centang `Dewi Anggraini` dan `Dewi Anggreni`
5. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
6. Verifikasi dialog Title "Remove Approvers", bullet kedua nama approver, "They will no longer be able to approve these requests.", "Are you sure you want to remove them?"
7. Klik `[Remove]`
8. Verifikasi toast "Success, approver has been removed."
9. Verifikasi Bulk Action Bar tertutup
10. Verifikasi seleksi di-reset

### TC-AC-RP-212: Bulk Remove Approver satu baris memakai dialog single

11. Pulihkan baseline automation: approver `Manage allocation` `Region Jawa` kembali `Dewi Anggraini` dan `Dewi Anggreni`, lalu muat ulang halaman
12. Klik node `Region Jawa`
13. Centang `Dewi Anggreni` saja
14. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
15. Verifikasi dialog yang tampil adalah "Remove Approver" (D-08)
16. Klik `[Cancel]`
17. Klik icon clear selection pada Bulk Action Bar

### TC-AC-RP-213: Bulk Remove Approver partial success

18. Pasang intercept respons: penolakan per baris pada baris `Dewi Anggraini` untuk submit Remove approver
19. Centang `Dewi Anggraini` dan `Dewi Anggreni`
20. Klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
21. Verifikasi toast "Success, approver has been removed. Some items were skipped."
22. Verifikasi baris yang berhasil (`Dewi Anggreni`) terhapus dari tabel Approvers
23. Verifikasi Bulk Action Bar tertutup
24. Verifikasi seleksi di-reset
25. Lepas intercept respons

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Langkah penghubung (S-03, S-09): langkah 11 (pemulihan baseline dan muat ulang), 12 (pilih ulang node sesudah muat ulang), 16 dan 17 (tutup dialog dan bersihkan seleksi), 18 dan 25 (pasang dan lepas intercept sebagai pemicu penolakan per baris).
- Temuan untuk QA:
  - TC-AC-RP-211 Expected a menulis "bullet kedua nama" tanpa nama; format komponen user pada bullet dialog memberi `Dewi A` untuk `Dewi Anggraini` dan `Dewi Anggreni` sehingga kedua bullet identik. Spec memverifikasi dialog tanpa menyebut teks bullet per nama.
  - TC-AC-RP-213 Expected "baris berhasil terhapus" tidak menyebut nasib baris yang ditolak (`Dewi Anggraini`); spec hanya mengasersi baris yang berhasil (`Dewi Anggreni`) terhapus dan tidak mengasersi baris yang ditolak.
  - TC-AC-RP-213 tidak menyebut penutupan dialog `[Remove]` pada partial success; tidak diasersi.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
