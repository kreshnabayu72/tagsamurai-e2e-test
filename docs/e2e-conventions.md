# Konvensi E2E Automation — TAG Samurai

Dokumen ini adalah sumber aturan untuk membuat spec e2e dari TC granular (`tc-[modul].md`). Skill `tagsamurai-e2e-generate-spec`, `tagsamurai-e2e-generate-script`, dan `tagsamurai-e2e-audit` merujuk ke sini.

Aturan framework TestSpectra (satu `it()` per file, zero-import, suffix platform, dan seterusnya) ada di skill bawaan `.claude/skills/*` dan tidak diulang di sini. Dokumen ini hanya memuat aturan khusus TAG Samurai.

Tanda `[VERIFIED]` = sudah dicek ke linter/CLI. Tanda `[REKOMENDASI]` = keputusan desain yang belum teruji di `spectra run` dan bisa diubah.

## 1. Alur Kerja

```
tc-[modul].md (TC granular, dikelola QA)
   -> seleksi TC yang layak diotomasi (bagian 2)
   -> spec.md (+ sourceTc)                   skill: tagsamurai-e2e-generate-spec
   -> web.test.ts, Page Object, Step, Fixture  skill: tagsamurai-e2e-generate-script
   -> spectra lint -> spectra run
   -> laporan audit traceability             skill: tagsamurai-e2e-audit
```

Sumber kebenaran tetap `tc-[modul].md`. Spec e2e adalah turunan. Perubahan isi TC dilakukan di `tc-[modul].md` dulu, baru disinkronkan ke spec.

## 2. Seleksi TC yang Diotomasi: Aturan Hibrida `[KEPUTUSAN 2026-09-28]`

Ada tiga lapisan: **BE** (API murni, `tc-[modul]-backend.md`), **FE** (API di-mock, `tc-[modul]-frontend.md`, ditulis dan dijalankan tim FE), dan **E2E** (semua nyata). Dokumen BE dan FE tetap terpisah seperti sekarang. E2E adalah lapisan tipis. Pertanyaan penentu untuk setiap TC: **apakah e2e menambah informasi yang tidak didapat dari lapisan lain?** Bukan "apakah lapisan lain sudah mencakupnya".

**Kelayakan teknis bukan kriteria seleksi `[KEPUTUSAN 2026-09-28]`:** kita menulis spec untuk apa yang seharusnya diuji, dan sengaja mendorong tim FE mengusahakan agar TC itu bisa dijalankan otomatis (dua sesi browser, simulasi hardware, akun entity khusus, mailbox uji, dan sebagainya). Semua kebutuhan (data, akun, kondisi environment, dan kemampuan teknis yang diminta) ditulis di `## Prerequisites`, yang menjadi sumber resmi bagi tim FE. `## Notes` hanya penjelasan tambahan dan tidak boleh menjadi satu-satunya tempat sebuah kebutuhan tercatat. Kalau akhirnya tidak bisa, spec ditandai `coverage.web: unsupported`, bukan dihapus. Tim FE yang menyiapkan environment-nya.

Kolom `Automation` di TC granular tidak cukup untuk menyeleksi, karena hampir semua TC bernilai `Automatable` (di `tc-user.md`: 537 dari 540).

**Masuk e2e:**
1. TC P0 dan alur bisnis kritis, walau lapisan lain sudah mencakupnya (overlap disengaja untuk alur yang paling berisiko).
2. TC yang efeknya harus dibuktikan dengan backend dan data nyata: cascade, persistensi, integritas satu record, data lintas layar atau modul.
3. Kasus murah: menambah sekitar 2 langkah di alur yang sudah ada (contoh: jalur Cancel sebelum Confirm, guard tombol disabled).

**Tidak masuk e2e:**
- Error, race, atau perubahan izin di tengah aksi yang hanya bisa dipicu lewat mock: 500, 403 di tengah dialog, partial failure, 404 karena dihapus admin lain. Kalau harus di-stub, itu tes FE.
- Copy dan state UI murni yang tidak butuh data nyata.
- Validasi kontrak API murni dan logika server yang tidak terjangkau UI (itu wilayah BE).
- Permukaan yang memang tidak bisa ditentukan hasilnya (contoh: konten pihak ketiga di luar kendali). Kata "Manual" atau ketidakpastian teknis di TC bukan alasan mengeluarkan TC.
- Permutasi data yang tidak menambah alur baru (digabung, lihat bagian 3).

**Data destruktif di environment automation:** environment yang dipakai run e2e adalah environment yang disiapkan dan diisolasi tim FE khusus untuk automation, bukan environment yang dipakai tester manual bersamaan. Karena itu, aksi Delete, Deactivate, atau Activate massal lewat Select All boleh dikonfirmasi sungguhan atas seluruh hasil Select All, termasuk saat kondisinya sengaja dibuat campur (banyak user, tersebar lintas halaman, status berbeda-beda) untuk menguji perilaku Select All itu sendiri (contoh: total `{N}`, exclude Default User dan Self, toggle ke Unselect All). Data yang dipakai tetap harus seeding milik automation, dicatat di Prerequisites.

**Pencatatan lapisan:** `docs/coverage/<Suite>.md` punya tabel "Lapisan per TC" dengan kolom FE (id TC FE dari tabel pemetaan di `tc-[modul]-frontend.md`) dan E2E (id spec). Kolom BE belum bisa diisi per TC granular, karena `tc-[modul]-backend.md` disusun dari kontrak API dan tidak merujuk id TC granular; BE dicatat pada tingkat endpoint. TC P0 yang hanya dicakup satu lapisan ditandai. Alasan "tidak diotomasi" wajib menyebut id TC FE yang mencakupnya, atau alasan lain yang spesifik.

Setiap TC granular yang tidak diotomasi dicatat alasannya di `docs/coverage/<Suite>.md` (bagian 8).

## 3. Efisiensi: Pengelompokan Spec `[KEPUTUSAN 2026-09-28]`

Prioritas utama adalah efisiensi run. Framework memaksa satu `it()` per file spec, jadi satu spec = satu alur yang bisa dijalankan sekali jalan. Soft assertion (assert gagal tidak menghentikan spec) dan report per langkah tersedia (dikonfirmasi tim, belum saya uji sendiri).

**Prinsip pengelompokan:**
1. **Satu spec = satu alur yang bisa dijalankan berurutan tanpa henti.** Kriterianya bukan permukaan yang sama, tapi apakah kasusnya bisa lanjut dalam alur yang sama: akun, role, dan entity sama, tidak butuh hardware, dan tidak mencampur pembuat data dengan bukan pembuat data. Kalau semua itu terpenuhi, gabung walau surface-nya berbeda (contoh: dialog konfirmasi di List, toggle di Detail, dan Modal Edit bisa satu spec). Pisah hanya kalau beda akun/entity/role, bergantung hardware, atau pembuat data vs non-pembuat data perlu dipisah.
2. **Screening (tanpa aksi) selalu di awal spec**, sebelum aksi lanjutan.
3. **Urutan di dalam sesi:** screening, lalu validasi yang diblokir (tidak membuat data), lalu aksi yang berhasil, lalu verifikasi di list.
4. **Variasi dari topik yang sama berurutan** (contoh: pilihan akses modul GS, FAMS, lalu entity lain).
5. **Aksi yang menghabisi atau merusak data (Delete, Bulk Delete, cascade purge, dan sejenisnya) selalu ditaruh paling akhir**, kalau spec yang sama masih punya kasus lain yang butuh baris itu tetap ada. Data yang sudah dihapus tidak bisa dipakai kasus setelahnya, jadi aksi itu ditunda sampai semua kasus lain selesai, walau sumbernya (TC granular) menyebutkannya lebih awal. Bonusnya, aksi ini di ujung sering sekaligus jadi cleanup untuk data seeding lain di spec yang sama.
6. **Kasus menutup form di akhir spec.** Menutup dalam keadaan dirty memakai form yang sudah dirty dari validasi, jadi tidak butuh buka tambahan. Menutup dalam keadaan bersih butuh form baru, jadi menjadi buka ulang terakhir. Jumlah minimal buka form sama dengan jumlah kejadian yang menutup form.
7. **Tiap validasi diakhiri submit yang diblokir** dan pengecekan tidak ada data tercipta. Satu submit valid di akhir bila memang perlu membuat data.
8. **Pakai fitur yang menghemat**, contohnya checkbox "Stay on this form after submitting" supaya beberapa create terjadi dalam satu sesi modal tanpa membuka ulang.
9. **Nilai batas atau nilai khusus** ditempel ke create yang assert-nya tidak bentrok. Satu nilai khusus per field per user, supaya penyebab kegagalan jelas.
10. **TC yang isinya terbelah lintas spec** (contoh: sisi Client dan sisi Principal) dicatat di `## Notes` kedua spec.

**Pisahkan spec hanya jika ada pemisah nyata:**
- Beda akun, role, atau entity (butuh login atau konteks lain).
- Bergantung pada hardware atau simulasi yang berisiko (contoh: scan RFID), supaya kegagalannya tidak menutupi hasil spec lain.
- Spec yang membuat data dan butuh cleanup dipisah dari spec yang tidak membuat data, supaya kegagalan keras di spec pembuat data tidak menutupi hasil spec lain. Soft assertion tidak menolong untuk kegagalan keras (elemen tidak ketemu, modal tidak terbuka).

**Tidak boleh:**
- Menggabung TC beda akun atau role kecuali ada Step khusus ganti akun.
- Spec yang bergantung pada data atau hasil spec lain. Setiap spec bisa jalan sendiri karena suite bisa `parallel: true`, dan urutan antar spec tidak dijamin (belum diverifikasi apakah runner mengikuti nomor folder). Jadi "screening di awal" dipenuhi dengan menaruhnya sebagai langkah pertama di dalam spec.

**Batas ukuran spec** bukan jumlah langkah, tetapi apakah bagian sesudahnya masih bermakna kalau bagian sebelumnya gagal keras. Beri subjudul (`### Screening`, `### Validation`, dan seterusnya) di dalam `## Test Steps` dan sebut id TC-nya di Notes atau di langkah, supaya report per langkah bisa dipetakan ke TC.

**Alur sekali jalan:** login, buka layar, dan seed data dilakukan sekali di hook. Isi `it()` hanya berisi aksi dan assert yang benar-benar diuji.

## 4. Setup dan Teardown

Aturan hook TestSpectra `[VERIFIED]`: `global-hooks/*` hanya jalan saat batch run dan **dilewati saat menjalankan satu spec**. `specs/<Suite>/hooks/*` selalu jalan.

| Kebutuhan | Tempat |
|---|---|
| Health check environment | `global-hooks/before` |
| Login akun aktor sekali per suite (lewat `seedSession` atau API) | `specs/<Suite>/hooks/before` |
| Reset state ringan (tutup dialog, kembali ke layar awal) | `specs/<Suite>/hooks/beforeEach` |
| Hapus data yang dibuat spec | `specs/<Suite>/hooks/afterEach` atau `after` |
| Alur bisnis berulang (buka menu, isi form) | `support/steps/<nama>/` |
| Utilitas teknis kecil | `support/actions/<nama>/` |

Hal yang tidak boleh: menaruh setup yang dibutuhkan satu spec di `global-hooks`, karena spec akan gagal saat dijalankan sendiri.

## 5. Data Uji

TC granular punya dua tabel data: **Pre-setup** (data tetap di environment, misalnya akun aktor dan user target) dan **Dinamis** (dibuat selama TC berjalan, dengan kolom Lifecycle).

- **Data Pre-setup** dirujuk lewat fixture `fixtures/<modul>.json`. Isinya identitas data, bukan rahasia.
- **Password dan token tidak boleh masuk fixture atau spec** (semua file di git). Simpan di environment variable lewat `executionConfig.environmentVariables` dan akses lewat `Spectra.env.NAMA`. `[REKOMENDASI]`, perlu keputusan tim tentang cara distribusinya.
- **Data Dinamis harus unik per run.** Nilai yang harus unik (email, employee ID) dibuat dengan suffix acak atau timestamp. Kalau tidak, run kedua gagal karena data sudah ada.
- **Lifecycle lintas TC dipecah.** Di TC granular ada data yang "dibuat di TC-A, diedit di TC-B, dihapus di TC-C". Di e2e setiap spec membuat datanya sendiri (lewat API di `before` atau `beforeEach`) dan tidak menumpang hasil spec lain.
- Data prasyarat sebisa mungkin dibuat lewat API, bukan lewat UI, supaya cepat dan tidak ikut gagal saat UI yang bukan fokus berubah.
- Data yang dibuat spec dibersihkan di `afterEach` atau `after`, dan tulis pembersihan sehingga tidak berasumsi setup berhasil penuh (aturan cascade hook).

## 6. Real Backend vs Mock

- Alur normal (happy path, validasi, permission) memakai backend asli `[REKOMENDASI]`.
- `Spectra.intercept()` hanya untuk kondisi yang tidak bisa dipicu dengan aman: error 500, timeout, dan response lambat. Skenario seperti ini biasanya sudah ada juga di `tc-[modul]-frontend.md`, jadi pastikan e2e memang menambah nilai.
- Target environment untuk e2e (staging, lokal, atau lainnya) belum ditentukan. Sementara `spectra.config.ts` masih menunjuk ke demo app bawaan.

## 7. Penamaan dan Struktur

**ID spec `[VERIFIED]` diterima linter, termasuk field `sourceTc`:**

```
TC-<ModulBesar>-<SubModul>-E2E-<NNN>-<slug-kebab>
contoh: TC-GS-USER-E2E-001-create-user-happy-path
```

- Prefix `<ModulBesar>-<SubModul>` mengikuti `foundation/tc-prefix-registry.md`, seragam dengan `TC-GS-USER-FE-004` dan `TC-GS-USER-BE-003`.
- `NNN` urut sendiri per modul, 3 digit, tidak pernah di-renumber. Lewat 999 cukup jadi 4 digit.
- Nomor e2e **tidak** harus sama dengan nomor TC granular, karena satu spec bisa menggabungkan beberapa TC. Hubungannya dicatat di `sourceTc`.
- Nama folder TC = `id` di frontmatter.

**Suite bersarang `specs/<ModulBesar>/<SubModul>/` (mengikuti struktur yang sudah ada di repo). Linter menerimanya dan pesan linter sendiri menyebut suite disusun lewat "directory hierarchy". Belum diuji lewat `spectra run`:**

```
specs/GlobalSettings/User/
  suite.md                          # id: suite-global-settings-user
  hooks/{before,beforeEach,afterEach,after}/web.hook.ts
  TC-GS-USER-E2E-001-create-user-happy-path/
    spec.md
    web.test.ts
```

- Folder modul besar dan submodul dalam PascalCase (`GlobalSettings/User`), satu `suite.md` per submodul. Kalau `suite.md` sudah ada, dipakai apa adanya dan tidak dibuat ulang.
- Page Object, Step, Action, Fixture tetap di folder bersama (`page-objects/`, `support/`, `fixtures/`). Nama entitas diberi awalan modul (`GlobalSettingsUserPage`, `createGlobalSettingsUser`). Jangan buat sub-folder modul di dalamnya karena folder itu discan otomatis untuk ambient types.
- Enam spec lama di `specs/GlobalSettings/User/` adalah percobaan dan diabaikan.

## 8. Traceability dan Coverage

Setiap spec punya frontmatter:

```yaml
id: TC-GS-USER-E2E-001-create-user-happy-path
title: <judul, sama persis dengan it()>
priority: Critical | High | Medium | Low
caseType: Positive | Negative | Edge
status: draft | ready-for-automation | automated | deprecated
sourceTc:
  - TC-GS-USER-13
coverage:
  web: automated
```

Mapping dari kolom TC granular `[REKOMENDASI]`:

| Kolom TC granular | Frontmatter spec |
|---|---|
| Priority P0 / P1 / P2 / P3 | Critical / High / Medium / Low |
| Tipe Positive / Negative | Positive / Negative |
| Tipe Boundary | Edge |
| Tipe Security | Negative |
| Spec gabungan, prioritas | ambil prioritas tertinggi dari TC sumber |
| Spec gabungan, caseType | ikut jenis alur utama yang dominan (lihat di bawah) |

**Aturan `caseType` untuk spec gabungan `[KEPUTUSAN 2026-09-26]`:** satu spec hanya punya satu `caseType`, dipilih dari jenis alur utama yang dominan, yaitu tujuan akhir alur spec tersebut, bukan jenis tiap TC sumber. Contoh: spec yang mengecek error tanggal kosong lalu berujung sukses membuat user berjenis `Positive`; spec yang seluruhnya menguji penolakan input berjenis `Negative`; spec yang seluruhnya menguji batas nilai atau karakter berjenis `Edge`. Kalau tidak ada yang dominan, pilih jenis TC dengan prioritas tertinggi.

**Arti `coverage` `[KEPUTUSAN 2026-09-26]`:** kolom `coverage.web` hanya menyatakan jenis pengujian di platform itu (`automated`, `manual`, atau `unsupported`), bukan progres. Spec yang dirancang untuk otomasi memakai `automated` sejak `draft`. Progres pengerjaan dibaca dari `status`, bukan dari `coverage`.

Field `status`: `draft` saat spec.md selesai, `ready-for-automation` setelah direview QA, `automated` setelah `web.test.ts` lulus lint dan lulus dijalankan.

Catatan cakupan per suite di `docs/coverage/<Suite>.md`: tabel TC granular ke spec e2e, atau ke alasan tidak diotomasi. `spectra lint` **tidak** memvalidasi isi `sourceTc`, jadi pengecekan ini dilakukan skill audit.

## 8a. Aturan `@step` `[VERIFIED]`

`spectra lint` menganggap `@step:<nama>` di spec.md tanpa `Step.<nama>()` di script sebagai error (`missing-step-call`), termasuk saat script belum ada. Karena itu spec berstatus `draft` ditulis tanpa `@step`, dan `@step` baru ditambahkan bersamaan dengan pembuatan Step dan script.

## 9. Aturan Kode

- **Label tombol mengikuti `foundation/process/prd-process/prd-conventions.md` §24.1, bukan disalin dari TC.** Form Create: `[Submit]` dan `[Clear Field]`. Form Edit: `[Save]` dan `[Clear Field]`. Modal Create dan Edit tidak punya `[Cancel]`, dan ditutup lewat `✕` di header atau `Esc`. `[Cancel]` hanya ada di dialog konfirmasi (contoh: unsaved changes, Delete, Deactivate), inline Cancel pending email change, dan modal Setup Column.
- Semua selector hanya di Page Object. Tidak ada `Spectra.get(...)` inline di `web.test.ts`.
- Selector diutamakan `~aria-label`, lalu `#testid`. Kalau elemen belum punya, minta dev FE menambahkannya. Jangan pakai xpath atau nth-child.
- Semua teks yang diassert diambil dari fixture atau konstanta resource, bukan diketik ulang di banyak spec.
- Tidak ada komentar di kode (aturan proyek).
- `spectra lint --strict <path>` harus bersih sebelum spec dianggap selesai.
