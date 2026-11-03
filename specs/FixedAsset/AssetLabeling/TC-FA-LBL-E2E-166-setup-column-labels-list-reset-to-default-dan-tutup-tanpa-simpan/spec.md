---
id: TC-FA-LBL-E2E-166-setup-column-labels-list-reset-to-default-dan-tutup-tanpa-simpan
title: "Setup Column Labels List: Reset to Default dan Tutup Tanpa Simpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-261
  - TC-FA-LBL-262
coverage:
  web: automated
---

# Setup Column Labels List: Reset to Default dan Tutup Tanpa Simpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex | Total Asset | Modified By |
  |---|---|---|---|
  | `High Priority` | `#EF4444` | 3 | `Sarah J` |
  | `Finance Department` | `#3B82F6` | 5 | `David K` |
  | `Audit Ready` | `#10B981` | 2 | `Sarah J` |
  | `Executive Asset` | `#8B5CF6` | 1 | `Michael W` |
  | `Maintenance Due` | `#F59E0B` | 4 | `David K` |
  | `Seasonal Event` | `#EC4899` | 0 | `Michael W` |
  | `Night Shift` | `#1E3A8A` | 0 | `Sarah J` |
  | `Warehouse Priority` | `#0EA5E9` | 0 | `Sarah J` |
  | `Field Kit` | `#84CC16` | 2 | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Labels List (diubah dan dipulihkan oleh langkah spec); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).

## Test Steps

### TC-FA-LBL-261: Reset to Default mengembalikan kelima kolom ke default setelah Save

1. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
2. Hapus centang `Color Hex`
3. Klik icon Pin `Label`
4. Seret `Modified By` ke posisi paling atas daftar
5. Klik `[Reset to Default]`
6. Verifikasi Live Preview kembali ke default: lima kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated` berurutan tanpa pin
7. Klik `[Save]`
8. Verifikasi tabel menampilkan lima kolom berurutan `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`
9. Verifikasi tidak ada kolom yang di-pin pada tabel
10. Tekan F5
11. Verifikasi konfigurasi default bertahan setelah F5: lima kolom berurutan `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated` tanpa pin

### TC-FA-LBL-262: Menutup Setup Column dengan ✕ atau Esc membuang perubahan preview

12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Hapus centang `Color Hex`
14. Klik icon `[✕]`
15. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (lima kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`)
16. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
17. Hapus centang `Total Asset`
18. Tekan Esc
19. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (lima kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`)

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Pembagian TC lintas spec: TC-FA-LBL-255 sampai TC-FA-LBL-257 ada di spec 069.
- Asersi "tanpa pin" pada tabel (langkah 9) diamati sebagai tidak ada kolom yang membeku; kelima kolom tampil pada langkah 8 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-LBL-261 Expected tidak memerinci cara mengamati "tanpa pin" pada tabel (tanpa scroll horizontal); spec mengasersi tidak ada kolom yang membeku dan icon Pin Live Preview kembali ke default.
