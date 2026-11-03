---
id: TC-FA-LBL-E2E-091-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-2-2
title: "Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-517
  - TC-FA-LBL-518
coverage:
  web: automated
---

# Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan), `Fixture.assetLabeling.akun.totalControlExtra`. Nama company, email akun (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), dan nama env password belum ada, disediakan tim FE; tidak diisi di spec. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Hook `after` suite mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #35 (hanya dibaca, di Company Extra, Pre-setup #56): label `Multi Status` (`#0EA5E9`) terpasang pada tiga aset dengan Status berikut; label `Multi Alpha` (`#6366F1`), `Multi Beta` (`#14B8A6`), `Multi Gamma` (`#F97316`) terpasang pada `Multi Asset - 34`, dan `Multi Alpha` juga pada `Multi Asset - 35` (hanya label itu):

  | Aset | Status | Label |
  |---|---|---|
  | `Multi Asset - 31` | `Borrowed` dan `Damaged` | `Multi Status` |
  | `Multi Asset - 32` | `Available` | `Multi Status` |
  | `Multi Asset - 33` | `Borrowed` | `Multi Status` |
  | `Multi Asset - 34` | - | `Multi Alpha`, `Multi Beta`, `Multi Gamma` |
  | `Multi Asset - 35` | - | `Multi Alpha` |

- Fixture label: `Fixture.assetLabeling.labelMultiAlpha` (`Multi Alpha`, Pre-setup #35).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Label` ditampilkan pada langkah 4 dan dipulihkan pada langkah 19); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.

## Test Steps

### TC-FA-LBL-517: Search Drawer mencocokkan nama label yang tersembunyi di balik +N more

1. Ketik Search `Multi Alpha` di kotak Search Labels List, tekan Enter
2. Klik chip `Multi Alpha` di kolom Label
3. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
4. Centang `Label`, lalu klik `[Save]`
5. Verifikasi `Multi Asset - 34` menampilkan badge `Multi Alpha` dan `Multi Beta` lalu chip `+1 more`
6. Verifikasi `Multi Asset - 35` menampilkan satu badge `Multi Alpha`
7. Ketik Search `Multi Gamma`, tekan Enter
8. Verifikasi hanya `Multi Asset - 34` (label `Multi Gamma` tersembunyi di balik `+1 more` tetap dicocokkan)
9. Verifikasi `Multi Asset - 35` tidak tampil
10. Klik `(←)` pada kotak Search

### TC-FA-LBL-518: Filter Drawer Label mencocokkan aset bila salah satu labelnya sama dengan opsi terpilih

11. Klik icon Filter di toolbar Drawer
12. Pilih `Label` = `Multi Gamma`, lalu klik `[Apply]`
13. Verifikasi hanya `Multi Asset - 34` (label ketiga di balik `+N more` cocok)
14. Buka panel Filter lagi (klik icon Filter di toolbar Drawer)
15. Klik `[Clear Field]`
16. Pilih `Label` = `Multi Beta` dan `Multi Alpha`, lalu klik `[Apply]`
17. Verifikasi `Multi Asset - 34` dan `Multi Asset - 35` (logika OR: `Multi Asset - 35` cocok lewat `Multi Alpha`)
18. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel
19. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
20. Tutup Drawer dengan `[✕]`, lalu klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search `Multi Alpha` pada Labels List untuk menemukan baris target (label tambahan Pre-setup #35 mungkin tidak berada di halaman pertama); membersihkan Search Drawer dan Filter sebelum TC berikutnya (S-09); pemulihan konfigurasi kolom di langkah 19; membersihkan Search Labels List di langkah terakhir. `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- TC-FA-LBL-518 dilanjutkan pada Drawer `Multi Alpha` yang sama dengan TC-FA-LBL-517 (satu pembukaan untuk TC tanpa perubahan state data).
- Pembagian TC lintas spec: TC-FA-LBL-513 sampai TC-FA-LBL-516 (label `Multi Status`) ada di spec 090.
- Temuan untuk QA:
  - TC-FA-LBL-518 menulis 'Buka panel lagi' tanpa menyatakan apakah `[Apply]` menutup Filter Panel; spec membuka panel lewat icon Filter mengikuti TC.
  - Company Extra (Pre-setup #56) memuat salinan label Pre-setup #12 plus seed tambahan; baris `Multi Alpha` dicari lewat Search dan posisi halamannya ditentukan tim FE.
