---
id: TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed
title: "Delete Group: Screening Dialog Konfirmasi, [Cancel], Delete via Elipsis Sidebar, Delete Node Assignable Berisi Aset Disposed, Delete Node Kosong, dan Cascade Subtree Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-218
  - TC-FA-GRP-219
  - TC-FA-GRP-220
  - TC-FA-GRP-221
  - TC-FA-GRP-222
  - TC-FA-GRP-239
coverage:
  web: automated
---

# Delete Group: Screening Dialog Konfirmasi, [Cancel], Delete via Elipsis Sidebar, Delete Node Assignable Berisi Aset Disposed, Delete Node Kosong, dan Cascade Subtree Kosong

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed per spec lewat API di `before`, tanpa aset dan tanpa user ter-scope): `Del Empty` (TC-218, TC-219, TC-220), `Del Sidebar` (TC-221), pohon `Cascade A` > `Cascade B` > `Cascade C` (TC-222), dan `Assign Del Own` (node Assignable level 1 milik spec ini, berisi hanya aset Disposed; target Delete TC-239; seeding disediakan tim FE/BE). Cleanup di `after` menghapus sisa data milik spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) dan membaca state aset Disposed (kolom group aset) lewat fixture BE.
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi.

## Test Steps

### TC-FA-GRP-218 dan TC-FA-GRP-220: Dialog konfirmasi Delete node kosong dan [Cancel]

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group
5. Ketik Search `Del Empty`, tekan Enter
6. Buka elipsis `⋯` baris `Del Empty` pada tabel, pilih `Delete`
7. Verifikasi dialog dengan title "Delete Group", bullet `Del Empty`, isi "Are you sure you want to delete it? This action cannot be undone.", tombol [Cancel] dan [Delete]
8. Klik [Cancel]
9. Verifikasi dialog tertutup
10. Verifikasi `Del Empty` tetap ada di tabel
11. Verifikasi tidak ada toast yang tampil
12. Buka Modal Changelog: Group
13. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
14. Tutup Modal Changelog: Group

### TC-FA-GRP-221: Delete via elipsis sidebar

15. Buka elipsis node `Del Sidebar` di sidebar, pilih `Delete`
16. Verifikasi dialog identik dengan dialog row action: title "Delete Group", bullet `Del Sidebar`, isi "Are you sure you want to delete it? This action cannot be undone.", tombol [Cancel] dan [Delete]
17. Klik [Delete]
18. Verifikasi toast sukses "Success, group has been deleted."

### TC-FA-GRP-239: Delete node Assignable berisi aset Disposed saja

19. Ganti isi kotak Search dengan `Assign Del Own`, tekan Enter
20. Buka elipsis `⋯` baris `Assign Del Own`, pilih `Delete`
21. Verifikasi dialog konfirmasi normal: title "Delete Group", bullet `Assign Del Own`, isi "Are you sure you want to delete it? This action cannot be undone." (aset Disposed tidak memblokir)
22. Klik [Delete]
23. Verifikasi toast sukses "Success, group has been deleted."
24. Verifikasi aset Disposed milik `Assign Del Own` tetap ada dan kolom group-nya kosong (dibaca lewat fixture BE)

### TC-FA-GRP-219: Delete node kosong, happy path

25. Ganti isi kotak Search dengan `Del Empty`, tekan Enter
26. Buka elipsis `⋯` baris `Del Empty`, pilih `Delete`
27. Klik [Delete]
28. Verifikasi dialog tertutup
29. Verifikasi toast sukses "Success, group has been deleted."
30. Verifikasi `Del Empty` hilang dari tabel
31. Verifikasi `Del Empty` hilang dari sidebar

### TC-FA-GRP-222: Delete node dengan subtree kosong, cascade seluruh descendant

32. Ganti isi kotak Search dengan `Cascade A`, tekan Enter
33. Buka elipsis `⋯` baris `Cascade A`, pilih `Delete`
34. Klik [Delete]
35. Verifikasi toast sukses "Success, group has been deleted."
36. Verifikasi `Cascade A`, `Cascade B`, dan `Cascade C` hilang dari tree sidebar

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 12, 14: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 5, 19, 25, 32 (Ketik atau ganti isi kotak Search dengan `Del Empty`, `Assign Del Own`, `Del Empty`, dan `Cascade A`, tekan Enter) menemukan baris yang dibuka elipsisnya; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: non-destruktif dan batal lebih dulu (TC-218, TC-220, TC-221 sidebar), lalu TC-239, dan Delete yang menghapus data paling akhir (TC-219, TC-222) sesuai S-10. TC-218 dan TC-220 memakai satu pembukaan dialog `Del Empty` yang sama (dialog dibuka sekali, diasersi, lalu dibatalkan); TC-219 membuka dialog baru.
- Spec berisi lebih dari 35 langkah. Alasan: lima TC Delete satu keluarga (dialog konfirmasi dan Delete node tanpa blokir), satu kelas (fungsional), satu dataset seed milik spec, dan tiap blok berdiri sendiri; langkah Search baris target dan baca-log berpola bukan asersi baru (bagian 3 prinsip 13).
- Klausa "tanpa toast, tanpa log" TC-220 diasersi pada langkah 11 dan 13 dengan baseline N0 (S-12); anchor positif: langkah 2 (entri lain tampil) dan langkah 10 (`Del Empty` tetap ada). Baris hilang pada langkah 30, 31, dan 36 memakai toast sukses sebagai anchor (8b butir 2).
- Langkah 24 (Verifikasi aset Disposed tetap ada) dipakai untuk Expected c TC-239; kemampuan baca state aset disediakan tim FE/BE (S-11).
- Temuan untuk QA:
  - TC-219 dan TC-222: Post Condition (baris Changelog Delete dan count group turun 1; 3 baris Delete cascade dengan Modified By = aktor) tidak punya langkah observasi di TC, sehingga tidak diasersi (S-01).
  - TC-239: Post Condition (nama Assign Del Own terbaca di Disposal Log/Changelog sebagai snapshot) tidak punya langkah observasi; tidak diasersi.
  - TC-220 menyebut "tanpa log" tanpa menyebut surface log; spec memakai Modal Changelog: Group.
