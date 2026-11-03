---
id: TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2
title: "Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-513
  - TC-FA-LBL-514
  - TC-FA-LBL-515
  - TC-FA-LBL-516
coverage:
  web: automated
---

# Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 1/2)

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

- Fixture label: `Fixture.assetLabeling.labelMultiStatus` (`Multi Status`, Pre-setup #35).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-513: Sel Status multi-badge di Drawer menampilkan badge berurut A-Z

1. Ketik Search `Multi Status` di kotak Search Labels List, tekan Enter
2. Klik chip `Multi Status` di kolom Label
3. Verifikasi `Multi Asset - 31` menampilkan dua badge berurut `Borrowed` lalu `Damaged` dalam satu sel
4. Verifikasi `Multi Asset - 32` menampilkan satu badge `Available`
5. Verifikasi `Multi Asset - 33` menampilkan satu badge `Borrowed`

### TC-FA-LBL-514: Sort Drawer kolom Status pada sel multi-badge memakai badge pertama

6. Klik header kolom `Status` satu kali
7. Verifikasi Ascending: `Multi Asset - 32` (`Available`), lalu `Multi Asset - 31` (`Borrowed` + `Damaged`), lalu `Multi Asset - 33` (`Borrowed`); `Multi Asset - 31` mendahului `Multi Asset - 33` karena badge pertama sama dan tie-breaker default Name
8. Klik header kolom `Status` sekali lagi (klik kedua)
9. Verifikasi Descending: `Multi Asset - 31`, `Multi Asset - 33`, lalu `Multi Asset - 32`
10. Klik header kolom `Status` sekali lagi (klik ketiga)
11. Verifikasi Netral kembali ke default Name A-Z: `Multi Asset - 31`, `Multi Asset - 32`, `Multi Asset - 33`

### TC-FA-LBL-515: Search Drawer mencocokkan badge Status mana pun pada sel multi-badge

12. Ketik Search `Damaged`, tekan Enter
13. Verifikasi keyword `Damaged` (badge kedua): hanya `Multi Asset - 31`
14. Ganti isi kotak search dengan `Borrowed`, tekan Enter
15. Verifikasi keyword `Borrowed`: `Multi Asset - 31` dan `Multi Asset - 33`
16. Klik `(←)` pada kotak Search

### TC-FA-LBL-516: Filter Drawer Status pada sel multi-badge mencocokkan aset bila salah satu badge sama dengan opsi terpilih

17. Klik icon Filter di toolbar Drawer
18. Buka dropdown `Status`
19. Verifikasi opsi dropdown `Status`: `Available`, `Borrowed`, dan `Damaged` (nilai badge distinct di tabel)
20. Pilih `Damaged`, lalu klik `[Apply]`
21. Verifikasi hanya `Multi Asset - 31` (badge kedua cocok)
22. Buka panel Filter lagi (klik icon Filter di toolbar Drawer)
23. Klik `[Clear Field]`
24. Pilih `Available` dan `Damaged`, lalu klik `[Apply]`
25. Verifikasi `Multi Asset - 31` dan `Multi Asset - 32` (logika OR dalam field)
26. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel, lalu tutup Drawer dengan `[✕]` dan klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search `Multi Status` pada Labels List untuk menemukan baris target (label tambahan Pre-setup #35 mungkin tidak berada di halaman pertama); membersihkan Search Drawer dan Filter sebelum TC berikutnya (S-09); langkah 26 menutup panel Filter, Drawer, dan Search Labels List.
- Seluruh TC memakai satu pembukaan Drawer `Multi Status` (tanpa perubahan state data); TC-FA-LBL-514 sampai TC-FA-LBL-516 dilanjutkan pada Drawer yang sama.
- Pembagian TC lintas spec: TC-FA-LBL-517 dan TC-FA-LBL-518 (label `Multi Alpha`, `Multi Beta`, `Multi Gamma`) ada di spec 091.
- Temuan untuk QA:
  - TC-FA-LBL-516 menulis 'Buka panel lagi' tanpa menyatakan apakah `[Apply]` menutup Filter Panel; spec membuka panel lewat icon Filter mengikuti TC dan menutup panel dengan klik area di luar panel pada langkah pemulihan.
  - TC-FA-LBL-514 hanya merinci urutan 3 aset; tie-breaker 'default Name' mengikuti tie-breaker yang sama pada TC-FA-LBL-361 (spec 098).
  - Company Extra (Pre-setup #56) memuat salinan label Pre-setup #12 plus seed tambahan; baris `Multi Status` dicari lewat Search dan posisi halamannya ditentukan tim FE.
