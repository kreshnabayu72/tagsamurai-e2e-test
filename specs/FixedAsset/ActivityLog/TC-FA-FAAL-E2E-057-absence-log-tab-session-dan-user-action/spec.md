---
id: TC-FA-FAAL-E2E-057-absence-log-tab-session-dan-user-action
title: "Absence Log: Membaca Tidak Menulis Baris dan Edit Tanpa Perubahan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-203
  - TC-FA-FAAL-251
coverage:
  web: automated
---

# Absence Log: Membaca Tidak Menulis Baris dan Edit Tanpa Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Pengecualian: langkah 24 membuka Edit Group di Settings > Groups.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12) dan Tab Session SS-01 sampai SS-11 (Pre-setup #11), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Group `Gedung B` ada (disediakan tim FE/BE) dan tidak diubah spec ini.
- Nilai uji TC-FA-FAAL-203: Search Tab User Action `Fixture.activity-log.searchKeywordUserAction`, Filter Action `Delete`, Search Tab Session `Budi`, Filter Note `Session started`, Sort kolom Date; keyword dan pilihan Filter menghasilkan sedikitnya satu baris pada tab masing-masing.
- Kemampuan teknis disediakan tim FE: penangkap unduhan browser (butir "Kemampuan teknis tambahan" di `suite.md`) untuk Download CSV; berkas hasil unduhan tidak diasersi di spec ini.
- Baseline (S-12): total baris tiap tab dibaca dari teks pagination `Showing x–y of N entries` sebelum aksi; Tab Session dan Tab User Action tidak tersaring saat total dicatat.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun observer.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-203: Melihat, Search, Filter, dan Download tidak menulis baris

1. Catat total baris Tab Session dari teks pagination (NS)
2. Klik tab User Action
3. Catat total baris Tab User Action dari teks pagination (NU)
4. Ketik Search `Fixture.activity-log.searchKeywordUserAction`, tekan Enter
5. Klik `(←)` pada kotak Search
6. Klik icon Filter, pilih `Delete` pada field Action, klik `[Apply]`
7. Klik header kolom Date untuk mengurutkan Tab User Action
8. Klik icon Download dan pilih `Download as CSV`
9. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)
10. Ketik Search `Budi`, tekan Enter
11. Klik `(←)` pada kotak Search
12. Klik icon Filter, pilih `Session started` pada field Note, klik `[Apply]`
13. Klik header kolom Date untuk mengurutkan Tab Session
14. Klik icon Download dan pilih `Download as CSV`
15. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)
16. Muat ulang halaman (F5)
17. Verifikasi Table Tools (icon Search, Filter, Download) tampil
18. Verifikasi total baris Tab Session sama dengan NS
19. Klik tab User Action
20. Verifikasi total baris Tab User Action sama dengan NU
21. Verifikasi halaman tidak punya aksi tulis

### TC-FA-FAAL-251: Edit tanpa perubahan tidak menulis baris

22. Buka Activity Log > User Action
23. Catat total baris Tab User Action dari teks pagination (NU)
24. Buka Edit Group `Gedung B` di Settings > Groups dan simpan tanpa mengubah nilai
25. Verifikasi toast `No changes to save.` muncul pada aksi Edit
26. Buka Activity Log > User Action
27. Verifikasi total baris Tab User Action sama dengan NU

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2 dan 19 (klik tab), langkah 5 dan 11 (mengosongkan Search), langkah 9 dan 15 (reset Search, Filter, Sort), langkah 22 dan 26 (membuka Tab User Action).
- Anchor absence: langkah 17 (Table Tools tampil setelah F5, bagian 8b butir 2) mendahului langkah 18 dan 20 untuk TC-FA-FAAL-203; toast `No changes to save.` (langkah 25) mendahului langkah 27 untuk TC-FA-FAAL-251. Total yang dicatat sebelum aksi (langkah 1, 3, 23) adalah baseline S-12.
- Langkah 21 memakai teks Expected TC apa adanya ("Halaman tidak punya aksi tulis").
- TC-FA-FAAL-255 (aksi Edit Group gagal tidak meninggalkan baris) ada di spec 076; TC-FA-FAAL-211, 218, 219 ada di spec 076 sebagai asersi absence Tab Session.
- Temuan untuk QA:
  - TC-FA-FAAL-203 menyebut "Search, Filter, Sort, dan Download CSV" tanpa kata kunci, pilihan Filter, atau kolom Sort; spec memakai keyword dan pilihan dari fixture/spec lain yang menghasilkan sedikitnya satu baris.
  - TC-FA-FAAL-203 berlabel Need API tanpa menyebut cara membaca jumlah baris selain "hitung baris"; spec membaca total dari teks pagination.
  - TC-FA-FAAL-251 langkah 1 tidak menyebut menu tempat Edit Group dibuka; spec memakai Settings > Groups.
