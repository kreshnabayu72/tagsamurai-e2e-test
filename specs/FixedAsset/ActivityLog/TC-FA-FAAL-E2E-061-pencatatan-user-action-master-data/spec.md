---
id: TC-FA-FAAL-E2E-061-pencatatan-user-action-master-data
title: "Pencatatan User Action: Category, Asset Name, Custom Asset ID, Label, dan Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-237
  - TC-FA-FAAL-238
  - TC-FA-FAAL-239
  - TC-FA-FAAL-240
  - TC-FA-FAAL-241
  - TC-FA-FAAL-243
  - TC-FA-FAAL-250
coverage:
  web: automated
---

# Pencatatan User Action: Category, Asset Name, Custom Asset ID, Label, dan Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor dan observer: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Pengecualian: tiap TC membuka Settings (Categories, Asset Name, Custom Asset ID, Asset Labeling, Custom Fields, Asset Transactional Policy) untuk aksinya lalu Activity Log > User Action.
- Data master, identitas dari `Fixture.activity-log.<kunci>` (fixture belum ada, disediakan tim FE), seluruhnya milik spec ini:
  - Category `Electronic Devices` tanpa dependensi (Pre-setup #22, TC-FA-FAAL-237).
  - Asset Name `Laptop` berkategori `Elektronik`, Borrow `On`, dan Self Service Borrow `On` (Pre-setup #23, TC-FA-FAAL-238 dan 243); Category `Furniture` ada.
  - Client utama (client Pre-setup #26): Custom Asset ID memakai Separator `Slash` (TC-FA-FAAL-239).
  - Label `Urgent` berwarna `#DC2626` (TC-FA-FAAL-240).
  - Custom Field `Warranty Note` berstatus Inactive (TC-FA-FAAL-241).
  - TC-FA-FAAL-250 berjalan di client kedua yang belum punya konfigurasi Custom Asset ID tersimpan, terpisah dari client Pre-setup #26 dan tidak bergantung urutan dengan TC-FA-FAAL-239; akun Total Control (Admin Alpha) client kedua, nama env var password, dan nilai Status, Separator, dan Segments Formula disediakan tim FE (TC tidak menyebutnya).
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada langkah 1; tiap Verifikasi baris baru juga memastikan total bertambah dari total terakhir yang dibaca.
- State yang diubah dan pemulihannya: Separator Custom Asset ID client utama dipulihkan ke `Slash` di hook `after`; konfigurasi Custom Asset ID yang dibuat TC-FA-FAAL-250 di client kedua dikembalikan ke keadaan tanpa konfigurasi oleh tim FE/BE di hook `after`; Category `Electronic Devices`, Category Asset Name `Laptop`, Borrow dan Self Service Borrow `Laptop`, warna Label `Urgent`, dan status Custom Field `Warranty Note` dipulihkan oleh tim FE/BE di hook `after`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Hook `after` mengembalikan sesi ke akun dan client default suite karena langkah 27 beralih ke client kedua.
- Penantian pencatatan: Verifikasi baris baru pertama tiap blok memakai idiom polling (muat ulang Tab User Action tiap 5 detik, batas 2 menit) sebagai pengganti langkah tunggu tersendiri.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log > User Action dan catat total baris dari teks pagination (N0)

### TC-FA-FAAL-237: Delete Category tercatat dengan New Value strip

2. Hapus category `Electronic Devices` di Settings > Categories
3. Tunggu aksi selesai
4. Buka Activity Log > User Action
5. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Delete`, Object `Categories`, Name `Electronic Devices`, Field `Category Name`, Old Value `Electronic Devices`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-238: Edit Category pada Asset Name tercatat satu baris per field

6. Ubah Category Asset Name `Laptop` menjadi `Furniture` di Settings > Asset Name dan simpan
7. Tunggu aksi selesai
8. Buka Activity Log > User Action
9. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `Asset Name`, Name `Laptop`, Field `Category`, Old Value `Elektronik`, New Value `Furniture`, Modified By `Admin A`

### TC-FA-FAAL-239: Edit Separator Custom Asset ID tercatat sebagai nama opsi

10. Ubah Separator menjadi `Dash` di Settings > Custom Asset ID dan simpan
11. Tunggu aksi selesai
12. Buka Activity Log > User Action
13. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `Custom Asset ID`, Name `—`, Field `Separator`, Old Value `Slash`, New Value `Dash`, Modified By `Admin A`

### TC-FA-FAAL-240: Edit Color Label tercatat satu baris

14. Ubah Color Label `Urgent` menjadi `#EF4444` di Settings > Asset Labeling
15. Tunggu aksi selesai
16. Buka Activity Log > User Action
17. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `Labels`, Name `Urgent`, Field `Color`, Old Value `#DC2626`, New Value `#EF4444`, Modified By `Admin A`

### TC-FA-FAAL-241: Activate Custom Field tercatat dengan Field Active

18. Aktifkan Custom Field `Warranty Note` di Settings > Custom Fields
19. Tunggu aksi selesai
20. Buka Activity Log > User Action
21. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Activate`, Object `Custom Fields`, Name `Warranty Note`, Field `Active`, Old Value `Inactive`, New Value `Active`, Modified By `Admin A`

### TC-FA-FAAL-243: Matikan Borrow menulis dua baris Edit untuk Borrow dan Self Service Borrow

22. Catat total dari Verifikasi langkah 21 sebagai Z0, lalu matikan switch Borrow untuk `Laptop` di Settings > Asset Transactional Policy
23. Tunggu aksi selesai
24. Buka Activity Log > User Action
25. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total Z0 + 2
26. Verifikasi dua baris teratas Tab User Action memuat, tanpa urutan, keduanya dengan Timestamp sama, Object `Asset Transactional Policy`, Name `Laptop`, Modified By `Admin A`: baris Action `Edit`, Field `Borrow`, Old Value `On`, New Value `Off`; dan baris Action `Edit`, Field `Self Service Borrow`, Old Value `On`, New Value `Off`

### TC-FA-FAAL-250: Satu aksi dengan tiga field menghasilkan tiga baris

27. Beralih ke client kedua tanpa konfigurasi Custom Asset ID tersimpan (terpisah dari client Pre-setup #26) sebagai Total Control (Admin Alpha)
28. Buka Activity Log > User Action pada client kedua dan catat total baris dari teks pagination (N1)
29. Buat Custom Asset ID baru di Settings > Custom Asset ID dengan Status, Separator, dan Segments Formula terisi
30. Tunggu aksi selesai
31. Buka Activity Log > User Action
32. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru dengan Action `Create`, Object `Custom Asset ID`, Name `—`, Field `Status`, Old Value `—`, total baris bertambah 3 dari N1 (tiga field)
33. Verifikasi baris baru dengan Action `Create`, Object `Custom Asset ID`, Name `—`, Field `Separator`, Old Value `—`
34. Verifikasi baris baru dengan Action `Create`, Object `Custom Asset ID`, Name `—`, Field `Segments Formula`, Old Value `—`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 7, 11, 15, 19, 23, 30; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Urutan TC: 237, 238, 239, 240, 241, 243, 250. TC-FA-FAAL-239 berjalan di client Pre-setup #26 dan TC-FA-FAAL-250 di client kedua tanpa konfigurasi Custom Asset ID (precondition b kedua TC); tidak ada ketergantungan urutan antara keduanya.
- Langkah penghubung (S-03): langkah 1, 4, 8, 12, 16, 20, 24, 31 (membuka Tab User Action), langkah 27 (beralih ke client kedua sesuai precondition b TC-FA-FAAL-250), langkah 28 (baseline total baris client kedua, S-12).
- Langkah 22 mencatat total Verifikasi langkah 21 sebagai Z0 (baseline TC-FA-FAAL-243, S-12) sebelum mematikan Borrow.
- Baseline S-12: langkah 1 mencatat N0 (client utama) dan langkah 28 mencatat N1 (client kedua). Tiap Verifikasi baris baru juga memeriksa total pagination lebih besar dari total pada Verifikasi sebelumnya; selisih eksak hanya diasersi untuk TC-FA-FAAL-243 (+2, langkah 25) dan TC-FA-FAAL-250 (+3, langkah 32).
- Langkah 25 dan 26 memecah Expected TC-FA-FAAL-243 per klausa (total Z0 + 2, lalu himpunan dua baris teratas dengan Timestamp sama); langkah 26 dibaca tanpa urutan karena kedua baris dapat jatuh dalam menit yang sama pada kolom Date (S-14); langkah 32 sampai 34 memecah TC-FA-FAAL-250 per Field (S-01).
- R-14: Modified By diasersi `Admin A` (First Name dan Last Initial).
- Temuan untuk QA:
  - Akun client kedua TC-FA-FAAL-250 tercatat di Pre-setup #30 TC sebagai disediakan tim FE; nama env var passwordnya ditetapkan tim FE (spec tidak memakai nama karangan).
  - TC-FA-FAAL-250 tidak menyebut nilai Status, Separator, dan Segments Formula, juga tidak menyebut Modified By dan New Value; spec tidak menambah asersi itu.
  - TC-FA-FAAL-243 menyebut "Timestamp sama" tanpa batas presisi; spec memakai nilai yang tampil di kolom Date.
  - Nama literal TC (`Laptop`, `Urgent`, `Warranty Note`) dipakai tanpa suffix per run; baris log immutable sehingga baris paling atas dijamin oleh Verifikasi total.
