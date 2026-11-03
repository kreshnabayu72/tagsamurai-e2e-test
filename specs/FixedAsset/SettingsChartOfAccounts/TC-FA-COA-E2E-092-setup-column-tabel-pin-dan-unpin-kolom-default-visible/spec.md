---
id: TC-FA-COA-E2E-092-setup-column-tabel-pin-dan-unpin-kolom-default-visible
title: "Setup Column Tabel: Pin dan Unpin Kolom Default Visible"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-191
coverage:
  web: automated
---

# Setup Column Tabel: Pin dan Unpin Kolom Default Visible

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data: tabel Chart of Accounts client default berisi akun Pre-setup P1 sampai P5 dan akun lain hasil seed (lihat Seed dan pemulihan di `suite.md`); lebar tabel membuat gulir horizontal tersedia.
- Kolom default Visible untuk langkah berulang (langkah 3 sampai 8):

  | Kolom |
  |---|
  | `Active` |
  | `Account Code` |
  | `Account Name` |
  | `Function` |
  | `Used By` |
  | `Last Used in Journal` |

- State yang diubah spec: tidak ada konfigurasi kolom yang disimpan; popup ditutup dengan ✕ tanpa `[Save]` (langkah 10). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-191: Pin dan unpin kolom default Visible

1. Klik header kolom Actions ⋯
2. Klik `Setup Column...`
3. Klik ikon Pin pada baris kolom `Active`
4. Gulir tabel horizontal ke kanan
5. Verifikasi kolom `Active` tetap di posisinya (beku di kiri) saat tabel digulir horizontal
6. Klik ikon Pin pada baris kolom `Active` untuk unpin
7. Gulir tabel horizontal ke kanan
8. Verifikasi kolom `Active` ikut bergeser setelah unpin
9. Ulangi langkah 3 sampai 8 untuk setiap kolom lain pada tabel Prerequisites (`Account Code`, `Account Name`, `Function`, `Used By`, `Last Used in Journal`)
10. Tutup modal dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (10 langkah nominal, sekitar 40 dengan ekspansi langkah 9): satu blok pin dan unpin diulang untuk enam kolom pada satu popup dan satu dataset (idiom 8b.7); `Verifikasi` tetap satu per klausa.
- Langkah 9 mengulang langkah 3 sampai 8 untuk lima kolom lain.
- Langkah penghubung (S-03): langkah 4 dan 7 (gulir tabel horizontal), langkah 10 (menutup popup tanpa `[Save]`; semua pin dibuang dan setiap kolom di-unpin lagi pada langkah 6).
- Spec ini hanya memuat TC-FA-COA-191.
- Temuan untuk QA:
  - TC-191 butir a menulis "beku di kiri" hanya sebagai penjelasan untuk kolom Active; butir b sampai f tidak menyebut sisi beku. Spec mengasersi "tetap di posisinya" untuk semua kolom.
