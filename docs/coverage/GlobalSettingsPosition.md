# Coverage E2E — Global Settings > User > Position

Sumber: `global-settings/position/TestCases/tc-position.md`.
Referensi kontrak: `global-settings/position/PRD/position.md` dan `global-settings/position/API/openapi.yaml`.
Klasifikasi backend: `global-settings/position/TestCases/tc-position-backend.md`.
Suite: `specs/GlobalSettings/Position/`.
Prefix Modul: `GS` + `POS` (`TC-GS-POS-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-position.md`: 236 baris.** Angka 246 yang muncul di
`foundation/tc-prefix-registry.md` adalah rentang migrasi ID, bukan jumlah TC. Angka yang dipakai di
dokumen ini selalu dihitung dari baris tabel yang benar-benar ada, bukan dari rentang ID.

---

## 1. Pemetaan TC Granular → Spec E2E (50 spec)

231 dari 236 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-POS-E2E-001 | Screening tab Position, default sort, dan data seed awal | FE+BE | 09, 15, 17 |
| TC-GS-POS-E2E-002 | Empty state genuinely kosong pada entitas tanpa Position | FE+BE | 18 |
| TC-GS-POS-E2E-003 | No result state dari pencarian tanpa match | FE+BE | 19 |
| TC-GS-POS-E2E-004 | Guided Tooltip tiga langkah pada tab Position | mock | 229, 230, 231, 232, 234 |
| TC-GS-POS-E2E-005 | Role Matrix: visibilitas tab dan kontrol per capability | FE+BE | 54, 55, 56, 57, 58, 59 |
| TC-GS-POS-E2E-006 | Role Matrix positif Create dan Edit | FE+BE | 122, 123 |
| TC-GS-POS-E2E-007 | Role Matrix positif Delete single dan Bulk Delete | FE+BE | 124, 125 |
| TC-GS-POS-E2E-008 | Role Matrix negatif: aktor tanpa akses | FE+BE | 60, 62 |
| TC-GS-POS-E2E-009 | Screening form Create dan aksesibilitas | FE+BE | 10, 11, 12, 38 |
| TC-GS-POS-E2E-010 | Validasi form Create, deteksi dirty, dan penutupan form | FE+BE | 33, 35, 37, 39, 43, 107, 249 |
| TC-GS-POS-E2E-011 | Create berhasil, populasi data, dan Stay on this form | FE+BE | 01, 16, 45, 100 |
| TC-GS-POS-E2E-012 | Boundary panjang dan trim pada form Create | FE+BE | 40, 41, 42 |
| TC-GS-POS-E2E-013 | Duplikat nama dan guard double-submit | FE+BE | 97, 250 |
| TC-GS-POS-E2E-014 | Screening dan validasi form Edit | FE+BE | 113, 34, 101, 103, 44, 108 |
| TC-GS-POS-E2E-015 | Boundary panjang dan trim pada form Edit | FE+BE | 104, 105, 106 |
| TC-GS-POS-E2E-016 | Edit berhasil dan submit no-op | FE+BE | 02, 22, 25, 114 |
| TC-GS-POS-E2E-017 | Edit bersamaan oleh dua aktor | FE+BE | 77, 78 |
| TC-GS-POS-E2E-018 | Delete single berhasil | FE+BE | 03, 21, 23 |
| TC-GS-POS-E2E-019 | Delete pada satu-satunya Position di entitas | FE+BE | 24 |
| TC-GS-POS-E2E-020 | Delete diblokir karena Position sedang dipakai | FE+BE | 96 |
| TC-GS-POS-E2E-021 | Race delete dan guard double-submit | FE+BE | 79, 80, 82 |
| TC-GS-POS-E2E-022 | Screening Bulk Action Bar dan protokol seleksi | FE+BE | 26, 199, 236, 239, 240 |
| TC-GS-POS-E2E-023 | Bulk Delete homogen dan collapse ke dialog single | FE+BE | 04, 29, 243 |
| TC-GS-POS-E2E-024 | Bulk Delete campuran dan seluruhnya terblokir | FE+BE | 27, 28, 244 |
| TC-GS-POS-E2E-025 | Race Bulk Delete antar aktor | FE+BE | 81 |
| TC-GS-POS-E2E-026 | Search, no result, dan interaksi dengan seleksi pada tabel utama | FE+BE | 64, 215, 216, 217, 186, 188, 189, 190, 191 |
| TC-GS-POS-E2E-027 | Interaksi Search, Filter, dan Sort | FE+BE | 66, 67, 71, 187 |
| TC-GS-POS-E2E-028 | Filter Last Updated | FE+BE | 116, 65, 247, 252, 72 |
| TC-GS-POS-E2E-029 | Sort dan state loading tabel | FE+BE | 69, 70 |
| TC-GS-POS-E2E-030 | Pagination dan page size | FE+BE | 30, 32, 245 |
| TC-GS-POS-E2E-031 | Persistensi state tabel dan independensi cache | FE+BE | 31, 119 |
| TC-GS-POS-E2E-032 | Download CSV dan XLSX pada tabel utama | FE+BE | 73 |
| TC-GS-POS-E2E-033 | Overlay visibilitas kolom dan search per kolom | FE+BE | 68, 117, 118, 131, 132 |
| TC-GS-POS-E2E-034 | Setup Column tabel utama T-POS-01 | FE+BE | 120, 121, 130, 133, 134, 135, 136, 137, 176 |
| TC-GS-POS-E2E-035 | Screening Popup Changelog: Position dan tombol aksi | FE+BE | 75, 112 |
| TC-GS-POS-E2E-036 | Search pada Popup Changelog | FE+BE | 218, 201, 202, 203, 204, 205, 206, 207, 219 |
| TC-GS-POS-E2E-037 | Filter Action, Position Name, Modified By, dan bulk action | FE+BE | 200, 208, 248, 209, 254, 210, 211, 212, 110 |
| TC-GS-POS-E2E-038 | Sort, pagination, dan download pada Popup Changelog | FE+BE | 178, 179, 180, 181, 182, 183, 184, 213, 214, 220, 246 |
| TC-GS-POS-E2E-039 | Visibilitas kolom dan search per kolom pada Popup Changelog | FE+BE | 111, 140, 141, 142, 146, 147, 151, 152, 156, 157, 161, 162, 166, 167, 171, 172, 251 |
| TC-GS-POS-E2E-040 | Setup Column Popup Changelog T-POS-02 | FE+BE | 138, 139, 143, 144, 145, 148, 149, 150, 153, 154, 155, 158, 159, 160, 163, 164, 165, 168, 169, 170, 173, 174, 175, 177 |
| TC-GS-POS-E2E-041 | Detail filter Action dan keterbatasan filter Popup Changelog | FE+BE | 185, 192, 193, 194, 195, 221, 222, 223, 224, 225, 227, 228, 235 |
| TC-GS-POS-E2E-042 | Pencatatan mutasi Position di tiga surface logging | FE+BE | 46, 48, 49, 50, 51, 52 |
| TC-GS-POS-E2E-043 | Sinkronisasi Position ke dropdown form User | FE+BE | 47, 98, 197 |
| TC-GS-POS-E2E-044 | Format tanggal mengikuti General Settings | FE+BE | 76, 198 |
| TC-GS-POS-E2E-045 | Parity hasil Create Missing Positions dengan create manual | FE+BE | 241, 242 |
| TC-GS-POS-E2E-046 | Master Data Count Limit sebagai ceiling | FE+BE | 85, 86, 196, 238 |
| TC-GS-POS-E2E-047 | Concurrent create duplicate antar dua aktor | FE+BE | 83 |
| TC-GS-POS-E2E-048 | Race Edit dan Delete pada record yang sama | FE+BE | 237 |
| TC-GS-POS-E2E-049 | Loading state, kegagalan server, dan respons lambat di seluruh endpoint | mock | 20, 53, 74, 93, 94, 95, 109, 226 |
| TC-GS-POS-E2E-050 | Fallback karakter terlarang saat DOM dimanipulasi | mock | 36, 102 |

## 2. TC hanya-BE (tidak masuk spec)

Lima TC bertanda `FE Test: -` di `tc-position.md`. Kolom itu berarti murni level backend
(validasi kontrak API atau logika server yang tidak terjangkau UI), jadi tidak ada spec yang bisa
membuktikannya lewat browser.

| TC | Section | Alasan tidak diotomasi |
|---|:---:|---|
| TC-GS-POS-63 | 3 | Penolakan `POST`/`PUT`/`DELETE /positions` langsung dengan `403 Forbidden` saat capability C/U/D tidak dimiliki. Butuh request API tanpa UI. Defense-in-depth PRD `position.md` §9.3. |
| TC-GS-POS-84 | 10 | Write pada entitas suspended/expired ditolak. Kondisi D1 harus dibuat lewat API admin console, tidak ada affordance UI untuk menaruhnya di posisi itu. |
| TC-GS-POS-87 | 9 | Konkurensi edit dan response `409 Conflict`. Butuh dua request editor yang benar-benar paralel dan observasi status respons, bukan dua sesi browser. |
| TC-GS-POS-88 | 9 | Race delete dan response `409 Conflict`. Alasan sama seperti TC-GS-POS-87. |
| TC-GS-POS-91 | 10 | Penegakan `master_data_count_limit` di server saat commit batch Import. Butuh eksekusi Import penuh lewat API. |

Konsekuensi: **section 9 "Security & Defense-in-Depth" tidak punya satu pun spec**, karena kedua
TC-nya (`87`, `88`) hanya-BE. Mintakan verifikasi lewat integration test di repo backend.

## 3. Sebaran per section TC

| Section | TC aktif | Tercakup | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Table List Flow | 12 | 12 | 0 |
| 3. Role Capability & Direct Access Flow | 9 | 8 | 1 |
| 4a. Create Position Flow | 24 | 24 | 0 |
| 4b. Edit Position Flow | 18 | 18 | 0 |
| 4c. Delete Position Flow (Single) | 10 | 10 | 0 |
| 4d. Bulk Delete Position Flow | 14 | 14 | 0 |
| 5a. Tabel Utama Position | 41 | 41 | 0 |
| 5b. Popup Changelog | 86 | 86 | 0 |
| 6. Pencatatan Audit Log & Multi-Surface Sync | 6 | 6 | 0 |
| 8. Cross-Module Sync | 7 | 7 | 0 |
| 9. Security & Defense-in-Depth | 2 | 0 | 2 |
| 10. Edge Case Matrix (Sisa D1–D10) | 7 | 5 | 2 |
| **Total** | **236** | **231** | **5** |

Section 2 dan 7 tidak ada di `tc-position.md`: section 2 (Mobile Experience & Responsive) dihapus
2026-09-26 dan section 7 (API Contract) tidak pernah punya TC granular, hanya tabel silang.

## 4. Temuan terhadap dokumen sumber

1. **Angka "246 TC" di `foundation/tc-prefix-registry.md` adalah batas atas rentang migrasi ID,
   bukan jumlah TC.** Jumlah baris TC aktif di `tc-position.md` adalah 236. ID tertinggi yang masih
   aktif adalah `TC-GS-POS-254`, dan ID `246` sendiri tidak lagi punya baris TC. Jadi angka 246 tidak
   boleh dipakai sebagai denominator cakupan di mana pun.
2. **Tujuh belas ID disebut di prosa tapi tidak punya baris TC.** Semua sudah dihapus atau
   direassign di `tc-position.md` sendiri, jadi ini bukan gap:
   `05`, `06`, `07`, `08`, `13`, `14`, `61`, `90`, `92`, `99`, `115`, `126`, `127`, `128`, `129`,
   `233`, `253`.
   - `05` sampai `08` adalah bagian CRUD E2E lama, dan `13` serta `14` bagiannya dipindahkan.
   - `126`, `127`, `128` adalah endpoint list/dropdown/export yang dipindahkan ke subsection CRUD E2E.
   - `115` dan `233` berasal dari section 2 Mobile yang dihapus.
   - `61` ditutup 2026-08-26 karena modul Position murni binary Show/Hidden dan tidak punya state
     Disabled.
   - `90` dihapus sebagai redundant, `92` dipindah ke section 6, `253` dihapus dan ID tidak dipakai
     ulang.
3. **`tc-position-frontend.md` (106 TC) tidak dipakai sebagai sumber spec.** Sesuai
   `docs/e2e-conventions.md` bagian 2 `[KEPUTUSAN 2026-09-30]`, spec e2e kini merangkap dokumen TC FE
   dan sumber kebenaran tetap `tc-position.md`. Dokumen `tc-position-frontend.md` yang ada bersifat
   legacy dan tidak dirujuk apa pun di dokumen ini.
4. **Kolom `FE Test` di TC granular tidak dipakai untuk seleksi.** Distribusinya
   131 `Need API`, 100 `UI Only`, 5 `-`. Kolom `Automation` hanya menyatakan apakah TC itu bisa
   diotomatisasi sama sekali, bukan apakah butuh API. Tiga spec `Mode: mock` ditentukan dari isi
   `Expected`, bukan dari kolom mana pun:
   `TC-GS-POS-E2E-004` (tampilan murni), `049` (loading, backend down, timeout),
   `050` (karakter terlarang via manipulasi DOM di luar jalur UI).
   `TC-GS-POS-20` (loading state) ikut dipindahkan ke spec `049`, bukan spec `001`, karena menangkap
   skeleton loader hanya andal lewat respons yang ditunda — memaksanya jadi mock, bukan FE+BE.
5. **Seed lebih dari 1000 Position dibutuhkan TC-GS-POS-240.** Auto-cap seleksi di 1000 baris
   filtered tidak dapat dibuktikan dengan jumlah data yang normal. Ini kebutuhan environment untuk tim
   FE, dicatat di `## Prerequisites` spec 022, bukan alasan menunda spec.
6. **`TC-GS-POS-229` bentrok dengan PRD `position.md` §4.7 dan dengan aturan terkunci Guided Tooltip.**
   `TC-GS-POS-229` menyebut walkthrough dua step dan step 2-nya menargetkan row action `Delete`.
   PRD §4.7 menyebut tiga step yang semuanya landmark permanen, yaitu tombol `[+ Position]`, area
   tabel, dan tombol `Changelog`.
   `foundation/functions/guided-tooltip.md` aturan terkunci nomor 2 melarang target berupa row action,
   dan nomor 4 mewajibkan Title serta Description berbahasa Inggris; PRD tidak boleh meng-override dua
   aturan ini.
   Keputusan untuk spec `TC-GS-POS-E2E-004`: pakai tiga step dari PRD §4.7. Isi Title dan Description
   diambil lewat fixture, tidak ditulis di spec, karena PRD §4.7 menuliskan description dalam bahasa
   Indonesian yang melanggar aturan terkunci nomor 4. Kontradiksi ini harus diputuskan pemilik PRD.
7. **Nama `total_control` dan `access_level` Total Control bukan dua role berbeda.**
   `PRD/position.md` §4.8 dan tabel Data Uji Pre-setup menuliskan role Total Control dua kali dengan
   dua nama. Keduanya adalah satu role, bukan dua role. Spec 005 memperlakukannya sebagai satu baris
   tabel role agar jumlah role yang diuji tidak melebihi jumlah akun yang benar-benar tersedia.
8. **Nilai harapan `TC-GS-POS-35` ambigu antara dua perilaku yang tidak bisa terjadi bersamaan.**
   Kolomnya berisi `Manager 😀`. Itu bisa berarti emoji berhasil diblokir sehingga field berisi
   `Manager `, atau berarti emoji masuk lalu inline error `Name contains invalid characters` muncul.
   PRD §9.9 menyebut karakter terlarang dicek langsung saat mengetik dan secara khusus menyebut emoji
   diblokir di level keystroke, sehingga keduanya tidak dapat berlaku bersamaan.
   Spec `TC-GS-POS-E2E-010` mengikuti PRD: emoji tidak pernah masuk field, dan karakter terlarang
   non-emoji diuji terpisah untuk memicu inline error. Sumber yang perlu diperbaiki adalah
   `tc-position.md`.
9. **PRD tidak menetapkan penanganan konflik pada Edit bersamaan.** PRD §9.6 menyatakan Edit Position
   idempotent, dan `TC-GS-POS-77` mengharapkan last-write-wins karena Admin B menyimpan lebih dulu.
   Tidak ada aturan optimistic locking, nomor versi, maupun pesan konflik yang ditetapkan di PRD
   mana pun. Spec `TC-GS-POS-E2E-017` karena itu memeriksa akibat yang benar-benar ditetapkan, yaitu
   nilai terakhir yang tersimpan, dan secara eksplisit melarang spec mengarang pesan konflik yang
   tidak ada di PRD. Kalau produk memutuskan memakai optimistic locking, ini spec yang harus diubah
   duluan, bersama PRD-nya.
10. **Edit no-op punya kontrak yang lebih ketat daripada sekadar toast.** PRD §9.6 catatan
    D-12/R-11 bersama `foundation/functions/changelog-entry.md` §8.5 menetapkan lima hal sekaligus,
    yaitu respons tetap berhasil, nol entri log di semua surface, toast netral `No changes to save.`
    yang bukan toast sukses, dropdown Position pada form User tidak berubah, dan re-check keunikan
    tetap mengecualikan record yang sedang diedit sehingga submit no-op tidak memicu
    `Name already exists` terhadap dirinya sendiri. `TC-GS-POS-25` hanya menyebut toast-nya. Spec
    `TC-GS-POS-E2E-016` menguji kelima hal itu, dan harus diubah bersama bila kontrak ini berubah.
11. **Wireframe Bulk Action Bar di PRD §4.2 tidak sesuai urutan baku platform, dan tidak menyebut
    elemen Server Select All sama sekali.** PRD §4.2 merender bar sebagai `counter | [Delete] | [✕]`,
    sedangkan `prd-conventions.md` §"Bulk Action Bar — Posisi & Urutan Elemen" menetapkan urutan baku
    dari kiri ke kanan, yaitu Bulk Action, counter, `Select All ({N} records)`, lalu ikon `✕`.
    PRD modul ini juga tidak pernah menyebut elemen `Select All ({N} records)`, padahal tiga TC
    (`TC-GS-POS-26`, `199`, `236`) dan platform conventions mengharuskannya ada. Spec 022 memakai
    urutan baku dari conventions dan mencatat wireframe PRD sebagai gap yang harus ditutup di PRD.
12. **`TC-GS-POS-26` menganggap elemen pertama Bulk Action Bar adalah tombol `[Delete]` langsung,
    sedangkan komponen platform adalah tombol dropdown `Bulk Action`.** Position hanya punya satu aksi
    massal sehingga isi dropdown-nya tetap satu, tapi PRD modul ini tidak pernah menyatakan apakah bar
    dirender sebagai dropdown atau sebagai tombol aksi langsung. Spec 022 memeriksa posisi elemen
    pertama dan urutan bar, bukan bentuk render-nya, supaya spec tidak terkunci pada satu interpretasi
    komponen yang belum ditetapkan di PRD.
13. **`TC-GS-POS-79` dan PRD §7.2 ayat 3 tidak konsisten untuk kasus record yang sudah tidak ada.**
    `TC-GS-POS-79` mengharapkan conflict popup dengan penyebutan `404`, sedangkan PRD §7.2 ayat 3
    menetapkan error 404 menutup modal otomatis, me-refresh tabel, dan memunculkan toast netral
    `This position is no longer available.`. PRD §9.4 D6 juga menyebut dialog untuk kasus 409, yaitu
    konflik versi, yang memang kondisi berbeda. Spec 021 mengikuti PRD §7.2 untuk kasus 404 dan tidak
    mengarang dialog untuk itu.

## 5. Kebutuhan environment yang diminta ke tim FE

Semua kebutuhan berikut sudah ditulis di `## Prerequisites` spec masing-masing, yang menjadi sumber
resmi sesuai `docs/e2e-conventions.md` bagian 2.

| Kebutuhan | Spec | Alasan |
|---|:---:|---|
| Namespace fixture `Fixture.globalSettingsPosition.*` | semua | Kontrak data dan caption agar tidak ada nilai literal yang diketik ulang antar spec. |
| `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` | semua | Kredensial login tidak boleh ditulis di spec maupun fixture. |
| Intercept respons per endpoint | 049, 050 | Simulasi backend down dan timeout. |
| Akun 7 role dari Tabel Data Uji Pre-setup | 005–008, 047 | Role Matrix dan konkurensi dua aktor. |
| Seed Position permanen `HR Business Partner` dan `Finance Manager` dengan user pemakai | 018, 019, 020, 021, 023, 024, 025 | Guard in-use `POS-LOGIC-02`, skenario bulk campuran, dan pemicu race status. |
| Fixture FE untuk memutus dan mengembalikan relasi Position ke user | 017, 021, 025 | Mengubah kondisi in-use di tengah race tanpa merusak prasyarat spec lain. |
| Seed lebih dari 1000 Position pada satu entitas | 022 | Auto-cap seleksi 1000 baris (TC-GS-POS-240). |
| Dua sesi browser simultan | 017, 021, 025, 047, 048 | Race Edit/Delete, double-submit, dan concurrent create. |
| Entitas kedua tanpa Position sama sekali | 002 | Empty state genuinely kosong. |
| Nilai `master_data_count_limit` entitas yang dapat diturunkan | 046 | Dialog "Limit Reached". |
| Kotak masuk uji untuk skenario import | 045 | Verifikasi hasil `[Create Missing Positions]`. |

## 6. Verifikasi silang

Pemetaan di atas diverifikasi dengan skrip terhadap 236 baris TC di `tc-position.md`:

- 231 ID TC unik tercatat, masing-masing tepat satu kali.
- 0 ID dobel.
- 0 ID yang tidak ada di `tc-position.md`.
- 5 ID tersisa persis himpunan TC hanya-BE.

`spectra lint` tidak memvalidasi isi `sourceTc`, jadi pengecekan ini diulang setiap kali spec
bertambah atau berubah.
