# Coverage E2E — Global Settings > General Settings

Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
Referensi kontrak: `global-settings/general-settings/PRD/general-settings.md` dan `global-settings/general-settings/API/openapi.yaml`.
Klasifikasi backend: `global-settings/general-settings/TestCases/tc-general-settings-backend.md`.
Suite: `specs/GlobalSettings/GeneralSettings/`.
Prefix Modul: `GS` + `GSET` (`TC-GS-GSET-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-general-settings.md`: 148 baris.** Ringkasan Cakupan pada bagian akhir
dokumen sumber menyatakan hal yang sama. Angka yang dipakai di dokumen ini selalu dihitung dari
baris tabel yang benar-benar ada, bukan dari rentang ID.

---

## 1. Pemetaan TC Granular → Spec E2E (46 spec)

131 dari 148 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-GSET-E2E-001 | Screening form General Settings dan 3 zona halaman | FE+BE | 01, 148 |
| TC-GS-GSET-E2E-002 | Loading skeleton, read failure, dan tombol retry | mock | 02, 05 |
| TC-GS-GSET-E2E-003 | State form: seed default vs data populated | FE+BE | 03, 04 |
| TC-GS-GSET-E2E-004 | Screening dan opsi dropdown kelima field | FE+BE | 06, 08, 09, 10, 11 |
| TC-GS-GSET-E2E-005 | Preview text live update kelima field | FE+BE | 12, 13 |
| TC-GS-GSET-E2E-006 | Tooltip info field senyap dan ringkas | FE+BE | 14 |
| TC-GS-GSET-E2E-007 | Guided Tooltip 2 langkah: konten verbatim dan siklus penuh | mock | 16, 17 |
| TC-GS-GSET-E2E-008 | Role Matrix positif untuk Read Only | FE+BE | 18 |
| TC-GS-GSET-E2E-009 | Role Matrix negatif: aktor tanpa akses | FE+BE | 19, 20 |
| TC-GS-GSET-E2E-010 | State tombol Save: clean vs dirty | FE+BE | 21, 22, 23, 24, 36 |
| TC-GS-GSET-E2E-011 | Save happy path dan boundary Session Idle Timeout maksimum | FE+BE | 25, 152 |
| TC-GS-GSET-E2E-012 | Dialog Change Currency: siklus penuh | FE+BE | 26, 27, 28, 29, 30 |
| TC-GS-GSET-E2E-013 | Revert currency pasca-cancel dan bypass gate dialog | FE+BE | 149, 150 |
| TC-GS-GSET-E2E-014 | Save gagal: timeout server dan double-submit | mock | 31, 39, 40 |
| TC-GS-GSET-E2E-015 | Dialog Unsaved Changes dan navigasi keluar | FE+BE | 151, 32, 33, 34, 35 |
| TC-GS-GSET-E2E-016 | Aksesibilitas form dan dialog | FE+BE | 37, 38 |
| TC-GS-GSET-E2E-017 | Screening modal Changelog dan pagination | FE+BE | 153, 41 |
| TC-GS-GSET-E2E-018 | Empty state changelog tanpa riwayat | FE+BE | 42, 59 |
| TC-GS-GSET-E2E-019 | No result state dari pencarian tanpa match | FE+BE | 43 |
| TC-GS-GSET-E2E-020 | Search per kolom changelog | FE+BE | 44, 45, 46, 47, 48, 49 |
| TC-GS-GSET-E2E-021 | Pola interaksi search box dan kolom hidden | FE+BE | 154, 50 |
| TC-GS-GSET-E2E-022 | Screening filter panel dan isi opsi | FE+BE | 51, 55, 56, 58 |
| TC-GS-GSET-E2E-023 | Filter Date rentang dan single date | FE+BE | 155, 52 |
| TC-GS-GSET-E2E-024 | Filter Field dan Modified By multi-select | FE+BE | 156, 53, 54, 61, 62, 63, 64, 65, 66, 67 |
| TC-GS-GSET-E2E-025 | Kombinasi search, filter, sort, pagination | FE+BE | 68, 69, 70, 71, 72, 73, 74 |
| TC-GS-GSET-E2E-026 | Populate realtime dan stale reference | FE+BE | 57, 60 |
| TC-GS-GSET-E2E-027 | Sorting 3-state untuk enam kolom | FE+BE | 75, 76, 77, 78, 79, 80 |
| TC-GS-GSET-E2E-028 | Screening overlay dan popup modal Setup Column | FE+BE | 81, 82 |
| TC-GS-GSET-E2E-029 | Setup Column hide/unhide dan guard kolom terakhir | FE+BE | 83, 84, 85, 86, 87, 88 |
| TC-GS-GSET-E2E-030 | Setup Column urutan drag | FE+BE | 89, 90, 91, 92, 93, 94 |
| TC-GS-GSET-E2E-031 | Setup Column pin/unpin | FE+BE | 95, 96, 97, 98, 99, 100 |
| TC-GS-GSET-E2E-032 | Setup Column reset, cancel, Esc layer, dan kolom pemicu statis | FE+BE | 101, 102, 157, 158 |
| TC-GS-GSET-E2E-033 | Download changelog sesuai filter dan kolom hidden | FE+BE | 103, 159 |
| TC-GS-GSET-E2E-034 | Download changelog gagal di sisi server | mock | 104 |
| TC-GS-GSET-E2E-035 | Pencatatan changelog di tiga surface | FE+BE | 105, 107, 108, 109 |
| TC-GS-GSET-E2E-036 | Snapshot immutability entri lama | FE+BE | 106 |
| TC-GS-GSET-E2E-037 | SSE push auto-refresh dan reconnect | FE+BE | 131, 132 |
| TC-GS-GSET-E2E-038 | SSE idle timeout refresh tanpa entri retroaktif | FE+BE | 134 |
| TC-GS-GSET-E2E-039 | Currency data existing: presisi dan tanpa konversi | FE+BE | 135, 136 |
| TC-GS-GSET-E2E-040 | Session Idle Timeout berlaku untuk sesi baru | FE+BE | 137 |
| TC-GS-GSET-E2E-041 | Session Idle Timeout independen dari auth | FE+BE | 138 |
| TC-GS-GSET-E2E-042 | Format admin console dan resolusi entitas staff | FE+BE | 139 |
| TC-GS-GSET-E2E-043 | Wallet exclusion selalu USD | FE+BE | 140 |
| TC-GS-GSET-E2E-044 | Tidak ada plan gating lintas tier | FE+BE | 145 |
| TC-GS-GSET-E2E-045 | Client suspended/expired: write diblokir | FE+BE | 146 |
| TC-GS-GSET-E2E-046 | Concurrent edit conflict 409 | FE+BE | 147 |

## 2. TC hanya-BE (tidak masuk spec)

Tujuh belas TC bertanda `PIC FE: -` / `PIC BE: v` di `tc-general-settings.md`. Kolom itu berarti
murni level backend (validasi kontrak API atau logika server yang tidak terjangkau UI), jadi tidak
ada spec yang bisa membuktikannya lewat browser.

| TC | Section | Alasan tidak diotomasi |
|---|:---:|---|
| TC-GS-GSET-110 | 6 | `GET /general-settings` — 200 Data Existing. Verifikasi respons API langsung, tanpa UI. |
| TC-GS-GSET-112 | 6 | `GET /general-settings` — 403 Forbidden untuk Create-Only. Panggilan API tanpa UI. |
| TC-GS-GSET-114 | 6 | `PUT /general-settings` — 200 Sukses. Panggilan API langsung. |
| TC-GS-GSET-115 | 6 | `PUT /general-settings` — 403 Bukan Total Control. Panggilan API langsung. |
| TC-GS-GSET-116 | 6 | `PUT /general-settings` — 403 Entitas Suspended/Expired. Kondisi D1 tidak terjangkau UI. |
| TC-GS-GSET-118 | 6 | `PUT /general-settings` — 422 Currency Code Empty. Validasi API. |
| TC-GS-GSET-119 | 6 | `PUT /general-settings` — 422 Time Zone Empty. Validasi API. |
| TC-GS-GSET-120 | 6 | `PUT /general-settings` — 422 Time Zone Invalid IANA. Butuh subuh IANA non-UI. |
| TC-GS-GSET-121 | 6 | `PUT /general-settings` — 422 Session Idle Timeout Empty. Validasi API. |
| TC-GS-GSET-122 | 6 | `PUT /general-settings` — 422 Session Idle Timeout Invalid Enum. Validasi API. |
| TC-GS-GSET-124 | 6 | `PUT /general-settings` — 422 Date Format Invalid Enum. Validasi API. |
| TC-GS-GSET-126 | 6 | `currencySymbol` dari client diabaikan, selalu server-derived. Verifikasi payload API. |
| TC-GS-GSET-133 | 7 | SSE tenant isolation — client lain tidak menerima event. Butuh dua koneksi SSE + observasi channel di level koneksi. |
| TC-GS-GSET-141 | 8 | Bypass — akses langsung `PUT` tanpa Total Control. Penyisipan request API langsung (defense-in-depth). |
| TC-GS-GSET-142 | 8 | Bypass — akses langsung `GET` tanpa permission. Penyisipan request API langsung. |
| TC-GS-GSET-143 | 8 | Tenant isolation — record entitas lain lewat manipulasi request. Butuh request API lintas entitas. |
| TC-GS-GSET-144 | 8 | `currencySymbol` tampering — payload berisi nilai custom. Butuh request API langsung. |

Konsekuensi: **section 6 "API Contract & Direct Backend Verification" dan section 8 "Security &
Defense-in-Depth" tidak punya spec sama sekali** (12 + 4 TC hanya-BE, plus TC-133). Mintakan
verifikasi lewat integration test di repo backend.

## 3. Sebaran per section TC

| Section | TC aktif | Tercakup | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Page Load Flow | 15 | 15 | 0 |
| 2. Role & Capability Access Flow | 3 | 3 | 0 |
| 3. Core Edit Flow | 24 | 24 | 0 |
| 4a. Tabel Utama (modul single-record) | — (N/A) | — | — |
| 4b. Modal Changelog — Table Rules | 71 | 71 | 0 |
| 5. Audit Log & Multi-Surface Sync | 5 | 5 | 0 |
| 6. API Contract & Direct Backend Verification | 12 | 0 | 12 |
| 7. Cross-Module Sync & Foundation Cascading | 10 | 9 | 1 |
| 8. Security & Defense-in-Depth | 4 | 0 | 4 |
| 9. Edge Case Matrix & Concurrency Sisa | 4 | 4 | 0 |
| **Total** | **148** | **131** | **17** |

Section 4a tidak ada TC di `tc-general-settings.md` per Ringkasan Cakupan: modul form single-record
tidak punya Tabel Utama (`general-settings.md` §5).

## 4. Temuan terhadap dokumen sumber

1. **Tujuh kurung ID yang kosong di rentang aktif bukan gap.** `07`, `15`, `111`, `113`, `117`,
   `123`, `125`, `127`, `129` (dan `130`) tidak punya baris TC di `tc-general-settings.md` — semua
   sudah dihapus atau direassign (mis. `111`, `113`, `117`, `123`, `125` dihapus per konfirmasi tim
   BE 2026-08-27, dan `15` adalah TC mobile yang dicabut 2026-10-01). Daftar lengkapnya ada di
   bagian Changelog dokumen sumber.
2. **Nama field currency adalah `Currency Code`, bukan "Currency".** Dipakai di form, kolom
   changelog, dan filter. Semua spec memakai `Currency Code`.
3. **Cancel dialog "Change Currency" tidak mereset nilai baru.** TC-GS-GSET-28 menetapkan bahwa
   setelah cancel, form tetap dirty dengan currency baru tersimpan (mis. USD), dan tombol Save tetap
   aktif. Spec `TC-GS-GSET-E2E-012` mengikuti ini; revert manual diuji terpisah di spec `013`.
4. **Guard bypass dialog di TC-GS-GSET-150.** Bila currency dikembalikan ke nilai tersimpan tetapi
   field lain berubah, Save menyala dan langsung hit `PUT` tanpa dialog "Change Currency". Diuji di
   spec `TC-GS-GSET-E2E-013`.
5. **Modal changelog punya 7 kolom**, bukan 6: `Date`, `Action`, `Field`, `Old Value`, `New Value`,
   `Modified By`, dan kolom `Actions (⋯)` terakhir. Kolom `Actions` tidak ada di checklist Setup
   Column (statis, selalu rightmost) — TC-GS-GSET-157, diuji di spec `028` dan `032`.
6. **Filter panel changelog tidak punya filter Action.** Hanya 3 grup: Date (Start/End), Field
   (default `All fields`, opsi verbatim `Currency Code | Time Zone | Date Format | Time Format |
   Session Idle Timeout`), dan Modified By (default `All users`). Spec 022 menguji isi opsi ini
   verbatim.
7. **Skema table body changelog yang dimodifikasi diam-diam dipakai untuk ambiguitas kolom.**
   TC-GS-GSET-82 (Screening Popup Modal) menyebut default sort `Date` descending; sort toolbar ada
   di tabel, bukan di popup setup column. Popup hanya berisi checklist + drag handle + pin + live
   preview.
8. **TC-GS-GSET-37 (aksesibilitas) menyebut "6 field form"**, padahal form General Settings hanya
   punya 5 field (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout). Spec
   `TC-GS-GSET-E2E-016` memakai 5 field dan mencatat penyebutan 6 sebagai ketidaksesuaian kecil di
   dokumen sumber yang perlu diperbaiki.
9. **Mode mock dipilih dari isi `Expected`, bukan dari kolom `FE Test`.** Empat spec `mock`:
   `002` (skeleton + read failure), `007` (guided tooltip walkthrough), `014` (save timeout +
   double-submit), `034` (download gagal server). Faktor pemersatu: skenario menangkap tampilan
   murni/simulasi kegagalan yang butuh kontrol penuh atas respons, bukan perilaku FE+BE nyata.

## 5. Kebutuhan environment yang diminta ke tim FE

Semua kebutuhan berikut sudah ditulis di `## Prerequisites` spec masing-masing.

| Kebutuhan | Spec | Alasan |
|---|---|:---:|
| Namespace fixture `Fixture.globalSettingsGeneralSettings.*` | semua | Kontrak data dan caption agar tidak ada nilai literal yang diketik ulang antar spec. |
| `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` | semua | Kredensial login tidak boleh ditulis di spec maupun fixture. |
| Intercept respons per endpoint | 002, 014, 034 | Simulasi backend down, timeout, dan download error. |
| Akun 7 role dari Tabel Data Uji Pre-setup | 008, 009, 045 | Role Matrix dan skenario client suspended. |
| Dua sesi browser simultan | 046 | Concurrent edit conflict 409. |
| SSE server-event yang bisa dikirim ke test client | 037, 038 | Push realtime dan idle-timeout refresh. |
| Browser yang mendukung SSE + kamera event channel | 037 | Verifikasi event ter-scope per tenant. |
| Data changelog historis (>100 baris) | 017, 025, 030 | Pagination 10/25/50/100 dan kombinasi filter. |
| Entitas kedua untuk tes tenant isolation (lewat BE) | 037 | Channel SSE antar client/tenant berbeda. |

## 6. Verifikasi silang

Pemetaan di atas diverifikasi dengan skrip terhadap 148 baris TC di `tc-general-settings.md`:

- 131 ID TC unik tercatat, masing-masing tepat satu kali.
- 0 ID dobel dalam `sourceTc` (muncul di lebih dari satu spec).
- 0 ID yang tidak ada di `tc-general-settings.md`.
- 17 ID tersisa persis himpunan TC hanya-BE (section 6 seluruhnya + TC-133 + section 8
  seluruhnya).

`spectra lint` tidak memvalidasi isi `sourceTc`, jadi pengecekan ini diulang setiap kali spec
bertambah atau berubah.