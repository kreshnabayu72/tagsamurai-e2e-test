---
id: TC-FA-RP-E2E-312-modal-changelog-transaction-role-terpisah-per-jenis-transaksi
title: Modal Changelog Transaction Role terpisah per jenis transaksi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1030
coverage:
  web: automated
---

# Modal Changelog Transaction Role terpisah per jenis transaksi

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group Company Alpha, node `IT Infrastructure`) dan #19 (seed Role Transaksi pada `IT Infrastructure` untuk sub-tab Disposal, Approver Pandu Wijaya; Require Approval OFF di semua node). Precondition tambahan yang tidak diasersi: penugasan Approver Transfer pada `IT Infrastructure` (Pandu Wijaya, seed Pre-setup #20 dengan toggle Transfer OFF) sebagai prasyarat aktivasi toggle (lihat Temuan untuk QA).
- Spec ini mengubah state: toggle `Require Approval for Disposal` dan `Require Approval for Transfer` pada `IT Infrastructure` diaktifkan lalu dinonaktifkan kembali (langkah 17 sampai 19); hook `after` memulihkan Pre-setup #19 dan #20 bila langkah pemulihan tidak tercapai. Entri Changelog Transaction Role bertambah dan tidak dapat dihapus (audit trail permanen).

## Test Steps

1. Klik Tab `Transaction Role`.
2. Klik node `IT Infrastructure` pada Sidebar Group Tree.
3. Klik sub-tab `Disposal`.
4. Aktifkan toggle `Require Approval for Disposal`.
5. Klik sub-tab `Transfer`.
6. Aktifkan toggle `Require Approval for Transfer`.
7. Klik ikon `[Changelog]` di baris sub-tab `Transfer`.
8. Verifikasi modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri `Require Approval — IT Infrastructure` untuk Transfer.
9. Verifikasi entri Disposal tidak tampil.
10. Verifikasi tidak ada kolom Object.
11. Tutup modal Changelog.
12. Klik sub-tab `Disposal`.
13. Klik ikon `[Changelog]` di baris sub-tab `Disposal`.
14. Verifikasi modal `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri Disposal.
15. Verifikasi entri Transfer tidak tampil.
16. Tutup modal Changelog.
17. Nonaktifkan toggle `Require Approval for Disposal`.
18. Klik sub-tab `Transfer`.
19. Nonaktifkan toggle `Require Approval for Transfer`.

## Notes

- Langkah penghubung (S-03): langkah 1 (berpindah ke Tab `Transaction Role`; halaman awal Tab `Total Control` dibuka hook `beforeEach` suite), 11 dan 16 (menutup modal), serta 17 sampai 19 (memulihkan toggle ke OFF).
- Langkah 8 dan 14 menjadi anchor positif bagi asersi absence langkah 9 dan 15 (bagian 8b butir 2).
- Temuan untuk QA:
  - Precondition TC 1030 hanya menyebut #18 dan #19; aktivasi toggle Transfer membutuhkan Approver Transfer pada `IT Infrastructure` yang disebut Pre-setup #20, tetapi #20 mendefinisikan Transfer sudah ON di `IT Infrastructure`, bertentangan dengan langkah 2 TC yang mengaktifkan toggle itu.
  - Changelog adalah audit trail permanen; TC mengasersi modal "hanya memuat" entri jenis transaksi aktif; spec mengasersi keberadaan entri jenis itu dan ketiadaan entri jenis lain tanpa menyebut jumlah absolut (S-12).
  - TC 1030 tidak menyebut pemulihan toggle sesudah selesai; spec menambah langkah pemulihan 17 sampai 19.
