---
id: TC-AC-ACC-E2E-153-delete-dialog-dan-izin-berubah-oleh-pelaku-lain
title: "Dialog Delete: Tidak Ter-refresh oleh Perubahan Sesi Lain dan Delete Ditolak karena Izin Delete Dicabut Saat Dialog Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-628
  - TC-AC-ACC-926
coverage:
  web: automated
---

# Dialog Delete: Tidak Ter-refresh oleh Perubahan Sesi Lain dan Delete Ditolak karena Izin Delete Dicabut Saat Dialog Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi UI yang diasersi; urutan blok = urutan akun, Step ganti akun eksplisit):

| Blok | Role | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | Total Control (Principal) A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `AC_TC_PASSWORD` | 628 |
| 2 | Active-Delete-Only A-07 (Manage active client: Delete + Read, exact-match Area Jakarta dan Cabang Menteng) | `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_DELETE_PASSWORD` | 926 |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Pelaku kedua (hanya memicu perubahan state dan hasilnya di sesi itu tidak diasersi, sehingga memakai sesi API, bukan konteks UI kedua dan tidak memakai `P-2`): Total Control A-01 lewat sesi API (`AC_TC_PASSWORD`) untuk mengubah PIC Name (TC-AC-ACC-628) dan mencabut permission Delete pada role "Manage active client" dari A-07 di Settings > Role & Permission (TC-AC-ACC-926). Sesi API aktor tidak dihitung sebagai sesi web; kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data: C-ROL-8 `PT Ubah Mitra 16` (Active, tanpa riwayat subscription, PIC Name awal `Budi Hartono`; PIC Name diubah ke `Rina Kartika` lalu dipulihkan ke nilai awal; Delete tidak dikonfirmasi); C-AST-10 `PT Hapus Uji Log` (Active, tanpa riwayat subscription, Default User tanpa App Access; permission Delete A-07 dicabut lalu dipulihkan; Delete ditolak sehingga Client tidak berubah). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang kedua Client di hook `before` dan `after` (C-AST-10 dikonsumsi oleh TC lain di spec TC-AC-ACC-425). Efek: Last Updated `PT Ubah Mitra 16` dan Last Updated role bertambah.
- Jeda amat TC-AC-ACC-628: 30 detik nyata sesuai TC (TC menyatakan durasinya; konvensi bagian 6 menetapkan 5 detik hanya sampai TC menyatakan durasi).
- State global yang diubah dan dipulihkan: permission role A-07 (pulihkan di hook `after`). Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-628: Dialog Delete tidak ter-refresh oleh perubahan sesi lain sebelum Confirm

1. Ketik Search `PT Ubah Mitra 16`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ubah Mitra 16` → klik `Delete` tanpa menekan `[Delete]`
3. Ubah PIC Name `PT Ubah Mitra 16` menjadi `Rina Kartika` lewat sesi API pelaku kedua hingga perubahan tersimpan
4. Tunggu 30 detik tanpa aksi apa pun di dialog
5. Verifikasi dialog Delete tetap terbuka dengan bullet `• PT Ubah Mitra 16`
6. Verifikasi tidak ada dialog lain yang muncul
7. Verifikasi tidak ada toast
8. Klik `[Cancel]`
9. Pulihkan PIC Name `PT Ubah Mitra 16` ke nilai awal `Budi Hartono` lewat sesi API pelaku kedua hingga perubahan tersimpan

### Blok Active-Delete-Only

10. Ganti akun: logout lalu login sebagai Active-Delete-Only A-07

#### TC-AC-ACC-926: Delete ditolak karena izin Delete dicabut saat dialog terbuka: toast error dan dialog tetap terbuka

11. Klik sub-tab Active, ketik Search `PT Hapus Uji Log`, tekan Enter
12. Klik `[⋯]` pada baris `PT Hapus Uji Log` lalu pilih `Delete`
13. Ketik `PT Hapus Uji Log` pada input "Type the client name to confirm" dan centang "I understand this action cannot be undone"
14. Cabut permission Delete pada role "Manage active client" dari A-07 lewat sesi API pelaku kedua hingga perubahan tersimpan
15. Klik `[Delete]`
16. Verifikasi toast error "Error, failed to delete client."
17. Verifikasi dialog "Delete Client" tetap terbuka
18. Klik `[Cancel]` pada dialog
19. Ganti isi Search dengan `PT Hapus Uji Log`, tekan Enter
20. Verifikasi baris `PT Hapus Uji Log` tetap tampil di sub-tab Active
21. Pulihkan permission Delete pada role "Manage active client" untuk A-07 lewat sesi API pelaku kedua hingga perubahan tersimpan

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Pelaku kedua memakai sesi API karena hasilnya di sesi itu tidak diasersi (konvensi bagian 3 prinsip 13, keputusan 2026-10-30); langkah pemicu ditulis "... hingga ... tersimpan" (R-20). TC asal menyebut sesi kedua UI dan label "Manual Only: dua sesi paralel".
- Langkah penghubung (tanpa awalan Verifikasi): `[Cancel]` penutup dialog (langkah 8 dan 18), pemulihan PIC Name dan permission (langkah 9 dan 21; Post Condition TC), ganti akun (langkah 10), dan Search yang menemukan baris target (R-16).
- Asersi absence "tidak ada dialog lain" dan "tidak ada toast" (langkah 6 dan 7) memakai dialog Delete yang masih terbuka (langkah 5) sebagai anchor positif (bagian 8b butir 2).
- Post Condition TC-AC-ACC-628 ("Pulihkan PIC Name") dan TC-AC-ACC-926 ("Permission Delete dipulihkan") sudah menjadi langkah.
- Temuan untuk QA:
  - TC-AC-ACC-628 langkah 2 menyebut sesi B mengubah PIC Name lalu Save lewat UI; spec memakai sesi API karena hasil di sesi itu tidak diasersi.
  - TC-AC-ACC-926 langkah 4 ("cabut permission ... dari A-07") tidak menyebut apakah sesi A-07 yang sedang aktif tetap hidup setelah pencabutan; spec mengikuti Expected (toast error, dialog tetap terbuka).
  - TC-AC-ACC-926 Precondition d menyatakan C-AST-10 dipakai juga oleh TC-AC-ACC-425 (dikonsumsi) dan perlu di-seed ulang bila sudah dihapus TC lain.
