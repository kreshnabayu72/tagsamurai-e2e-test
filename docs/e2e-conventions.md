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

## 2. Seleksi TC: Dokumen E2E Merangkap TC FE `[KEPUTUSAN 2026-09-30]`

Dokumen TC per submodul ada tiga: **TC ori** (`tc-[modul].md`, sumber semua TC), **TC BE** (`tc-[modul]-backend.md`, kasus hanya-BE), dan **TC E2E** (kumpulan `spec.md` di repo ini). Spec e2e sekarang merangkap dokumen TC FE: `tc-[modul]-frontend.md` tidak dibuat lagi untuk modul yang mengikuti pola ini, dan integration test FE (API di-mock, di repo FE) memakai `spec.md` sebagai acuannya. Pembersihan dokumen `tc-[modul]-frontend.md` yang sudah ada dilakukan terpisah dan tidak dikerjakan bersama pekerjaan spec.

**Satu-satunya TC yang tidak masuk spec adalah TC hanya-BE** (validasi kontrak API dan logika server yang tidak terjangkau UI). Semua TC lain masuk spec, termasuk tampilan murni, tooltip, Setup Column, hover, keystroke, dan kegagalan server (500, timeout).

Spec dibagi menurut **mode eksekusi**, karena persiapannya berbeda:
- **Spec FE+BE:** dijalankan TestSpectra terhadap backend nyata, dengan data seeding di backend.
- **Spec hanya-FE:** dijalankan tim FE sebagai integration test dengan API di-mock (kasus 500, timeout, payload izin, tampilan murni). Ditandai dengan baris `Mode: mock` di `## Prerequisites`. Kebutuhan mock (respons apa yang dipaksa, di endpoint mana) ditulis di Prerequisites juga.

Spec hanya-FE dikelompokkan per layar atau topik UI (contoh: "Setup Column", "Tooltip dan disabled state", "Foto profil: hover dan staged", "Custom Field: input"), bukan satu spec per TC dan bukan satu spec raksasa.

**Kelayakan teknis bukan kriteria seleksi `[KEPUTUSAN 2026-09-28]`:** kita menulis spec untuk apa yang seharusnya diuji, dan sengaja mendorong tim FE mengusahakan agar TC itu bisa dijalankan otomatis (dua sesi browser, simulasi hardware, akun entity khusus, mailbox uji, dan sebagainya). Semua kebutuhan (data, akun, kondisi environment, dan kemampuan teknis yang diminta) ditulis di `## Prerequisites`, yang menjadi sumber resmi bagi tim FE. `## Notes` hanya penjelasan tambahan dan tidak boleh menjadi satu-satunya tempat sebuah kebutuhan tercatat. Kalau akhirnya tidak bisa, spec ditandai `coverage.web: unsupported`, bukan dihapus. Tim FE yang menyiapkan environment-nya.

Kolom `Automation` di TC granular tidak cukup untuk menyeleksi, karena hampir semua TC bernilai `Automatable` (di `tc-user.md`: 537 dari 540).

**Masuk spec (semua kecuali hanya-BE):**
1. TC yang efeknya harus dibuktikan dengan backend dan data nyata: cascade, persistensi, integritas satu record, data lintas layar atau modul (spec FE+BE).
2. TC yang perilakunya di browser: tampilan, tooltip, state disabled, hover, keystroke, Setup Column, retensi state (spec hanya-FE, atau langkah tambahan di spec FE+BE bila murah).
3. Kegagalan server (500, timeout), race, dan perubahan izin di tengah aksi, termasuk yang butuh pemicu khusus. Kalau dipicu lewat mock, masuk spec hanya-FE (`Mode: mock`). Kalau bisa dipicu di backend nyata, masuk spec FE+BE.
4. Kasus murah: menambah sekitar 2 langkah di alur yang sudah ada (contoh: jalur Cancel sebelum Confirm, guard tombol disabled).

**Tidak masuk spec:**
- Validasi kontrak API murni dan logika server yang tidak terjangkau UI (itu wilayah BE).
- Permutasi data yang tidak menambah alur baru (digabung, lihat bagian 3). Ini penggabungan, bukan pengecualian: id TC-nya tetap dicatat di `sourceTc`.

**Hambatan teknis bukan alasan mengeluarkan TC:** data, akun, waktu, kuota, race, kegagalan server, hardware, atau konfigurasi khusus tidak pernah menjadi alasan. Kebutuhannya ditulis di `## Prerequisites` dan tim FE yang menyiapkan environment. Kata "Manual" atau ketidakpastian teknis di TC juga bukan alasan.

**Data destruktif di environment automation:** environment yang dipakai run e2e adalah environment yang disiapkan dan diisolasi tim FE khusus untuk automation, bukan environment yang dipakai tester manual bersamaan. Karena itu, aksi Delete, Deactivate, atau Activate massal lewat Select All boleh dikonfirmasi sungguhan atas seluruh hasil Select All, termasuk saat kondisinya sengaja dibuat campur (banyak user, tersebar lintas halaman, status berbeda-beda) untuk menguji perilaku Select All itu sendiri (contoh: total `{N}`, exclude Default User dan Self, toggle ke Unselect All). Data yang dipakai tetap harus seeding milik automation, dicatat di Prerequisites.

**Pencatatan lapisan:** `docs/coverage/<Suite>.md` punya tabel "Lapisan per TC" dengan kolom Spec (id spec) dan Mode (`FE+BE` atau `mock`). Kolom BE belum bisa diisi per TC granular, karena `tc-[modul]-backend.md` disusun dari kontrak API dan tidak merujuk id TC granular; BE dicatat pada tingkat endpoint. Kolom id TC FE lama (`FE-xxx`) dipertahankan sementara sebagai referensi selama `tc-[modul]-frontend.md` belum dibersihkan.

Setiap TC granular yang tidak masuk spec (hanya-BE) dicatat alasannya di `docs/coverage/<Suite>.md` (bagian 8).

## 3. Efisiensi: Pengelompokan Spec `[KEPUTUSAN 2026-09-28]`

Prioritas utama adalah efisiensi run. Framework memaksa satu `it()` per file spec, jadi satu spec = satu alur yang bisa dijalankan sekali jalan. Soft assertion (assert gagal tidak menghentikan spec) dan report per langkah tersedia (dikonfirmasi tim, belum saya uji sendiri).

**Prinsip pengelompokan:**
1. **Satu spec = satu topik aksi yang bisa dijalankan berurutan tanpa henti `[KEPUTUSAN 2026-09-29]`.** Digabung kalau topiknya sama, akun/role/entity sama, tidak butuh hardware, dan tidak mencampur pembuat data dengan bukan pembuat data. Permukaan yang berbeda tidak menghalangi penggabungan. **Topik aksi yang berbeda dan masing-masing butuh kondisi data yang bervariasi dipisah walau akunnya sama**: Delete, Toggle Active, dan Remove Access adalah tiga spec. Topik yang berbagi dataset yang sama tetap satu spec (contoh: Search, Filter, Sort, Pagination, dan Download di List).
2. **Screening (tanpa aksi) selalu di awal spec**, sebelum aksi lanjutan.
3. **Urutan di dalam sesi:** screening, lalu validasi yang diblokir (tidak membuat data), lalu aksi yang berhasil, lalu verifikasi di list.
4. **Variasi dari topik yang sama berurutan** (contoh: pilihan akses modul GS, FAMS, lalu entity lain).
5. **Aksi yang menghabisi atau merusak data (Delete, Bulk Delete, cascade purge, dan sejenisnya) selalu ditaruh paling akhir**, kalau spec yang sama masih punya kasus lain yang butuh baris itu tetap ada. Data yang sudah dihapus tidak bisa dipakai kasus setelahnya, jadi aksi itu ditunda sampai semua kasus lain selesai, walau sumbernya (TC granular) menyebutkannya lebih awal. Bonusnya, aksi ini di ujung sering sekaligus jadi cleanup untuk data seeding lain di spec yang sama.
6. **Kasus menutup form di akhir spec.** Menutup dalam keadaan dirty memakai form yang sudah dirty dari validasi, jadi tidak butuh buka tambahan. Menutup dalam keadaan bersih butuh form baru, jadi menjadi buka ulang terakhir. Form yang sudah diisi lalu dikosongkan lewat `[Clear Field]` tidak dihitung bersih untuk keperluan isolasi: kasus menutup bersih memakai form baru. Ini hanya soal isolasi state; dialog `Unsaved Changes` mengikuti PRD (form Create yang kosong tidak dirty, jadi menutupnya tidak memunculkan dialog). Pengecualian: kasus yang memang menguji pengosongan atau revert itu sendiri (contoh: kembali ke nilai tersimpan) boleh melanjutkan form yang sama. Jumlah minimal buka form sama dengan jumlah kejadian yang menutup form.
7. **Tiap validasi diakhiri submit yang diblokir** dan pengecekan tidak ada data tercipta. Satu submit valid di akhir bila memang perlu membuat data.
8. **Pakai fitur yang menghemat**, contohnya checkbox "Stay on this form after submitting" supaya beberapa create terjadi dalam satu sesi modal tanpa membuka ulang.
9. **Nilai batas atau nilai khusus** ditempel ke create yang assert-nya tidak bentrok. Satu nilai khusus per field per user, supaya penyebab kegagalan jelas.
10. **TC yang isinya terbelah lintas spec** (contoh: sisi Client dan sisi Principal) dicatat di `## Notes` kedua spec.
11. **Select All lalu Bulk Delete masuk ke spec Delete, di akhir spec `[KEPUTUSAN 2026-09-29]`.** Aksi ini menghapus semua user di environment kecuali Default User dan akun yang login, termasuk user seeding milik spec lain. Karena itu spec Delete wajib berjalan sesudah spec lain selesai dan tidak paralel dengannya. Runner belum terbukti mengikuti nomor folder, jadi cara memisahkannya (suite atau tahap run sendiri) diputuskan di tahap script.
12. **Blokir karena kondisi data dipisah menjadi spec sendiri per topik `[KEPUTUSAN 2026-09-29]`.** Kasus yang ditolak sistem karena kondisi data target (contoh: TAG sudah dipasang user lain, Resend masih dalam cooldown, Reset Authenticator pada user yang belum enrolled, kuota atau batas seleksi tercapai) butuh data prasyarat khusus yang berbeda dari alur normal, sehingga tidak digabung dengan alur normal. Yang tetap digabung dengan alur normal adalah validasi field (wajib, format, panjang, duplikat) dan blokir berbasis identitas atau role (Default User, akun sendiri, target Total Control), karena tidak butuh data khusus. Aksi yang tidak punya blokir data tidak perlu spec blokir: `USER-LOGIC-05` menetapkan Deactivate, Remove Access, dan Delete selalu warn lalu proceed.

13. **Kelas harness yang berbeda dipisah, walau layar dan topiknya sama `[KEPUTUSAN 2026-10-08]`.** Asal: `gap-spec/gap-spec.md` (MFA, ActivityLog, Division, LoginPassword, Role, ResetPassword), pola yang sama berulang di 6 modul. Spec screening atau fungsional biasa tidak boleh memuat TC dari kelas berikut; tiap kelas jadi spec sendiri:
    - **a. Defense-in-depth:** injeksi SQL/XSS, direct API tampering atau 403, manipulasi token, bypass server-side (token dibuang dari payload).
    - **b. Fault injection / resilience:** HTTP 5xx, timeout, outage penyedia (reCAPTCHA, IdP), rollback DB. Menahan respons hanya untuk mengamati state UI (loading, saving, spinner) bukan kelas b dan boleh berada di spec fungsional; yang masuk kelas b adalah kegagalan atau timeout yang dipaksakan. `Mode: mock` bila seluruh API di-mock; intercept parsial di atas backend nyata atau asersi state backend → `FE+BE` dengan intercept (bagian 6); kegagalan sisi server atau penyedia yang tidak bisa di-intercept tetap `FE+BE`.
    - **c. Multi-konteks:** multi-tab atau device, race antar-sesi, dua tenant, dua admin, flood rate-limit (429).
    - **d. Harness eksternal:** polling mail-catcher, decode QR, hardware biometrik, SSO IdP, time-travel atau TTL, background job.
    - **e. Volume data khusus:** kuota Selection Limit, data ≥ N record, retensi lintas tahun (perluasan prinsip 12).
    - **f. Binary buffer:** isi file CSV/XLSX (BOM, header, format) dipisah dari kegagalan ekspor.
    - **g. Asersi absence** ("baris log TIDAK muncul") dipisah dari asersi pencatatan (Status/Note spesifik). Pengecekan isolasi log per aktor ("entri aktor A tidak muncul di System Log aktor B") adalah asersi kepemilikan log, bukan kelas g, dan boleh berada di spec pencatatan. Asersi jumlah ("tepat 1 entri Delete per brand") bukan absence dan boleh berada di spec fungsional.
    - **h. State tenant:** write-lockdown (Client Suspended, Expired) dipisah dari verifikasi baca murni.

    **Cara menggabung antar-aksi:** kelas ringan (a tanpa harness eksternal, b) cukup satu spec per kelas per modul, misalnya satu spec "Resilience" untuk Create, Edit, Delete, dan Export, selama tidak melewati batas smell. Tidak perlu satu spec per aksi, karena tiap spec menambah login, hook, dan cleanup. Kelas berat (c, d, e) satu spec per jenis harness: mail-catcher tidak digabung dengan multi-tab, dan multi-tab tidak digabung dengan dua tenant.
    Setup Column, Bulk Action Bar, dan Search/Filter/Sort tetap satu spec selama dataset dan harness-nya sama; pecah hanya kalau melewati batas kelas di atas atau bagian sesudahnya tidak lagi bermakna bila bagian sebelumnya gagal keras (batas ukuran di bawah).
    **Pengecualian:** TC yang konteksnya bergantung pada state berat yang baru dibangun langkah sebelumnya di spec asal (contoh: lock tahap 1 jam, handoff MFA) boleh tetap di sana; catat alasannya di `## Notes`.
    **Smell, bukan kriteria:** spec melewati sekitar 35 langkah atau memuat lebih dari satu kelas harness wajib ditinjau ulang sebelum rencana diajukan.

**Pisahkan spec hanya jika ada pemisah nyata:**
- Topik aksi berbeda dengan kondisi data yang bervariasi (prinsip 1).
- Kasus blokir karena kondisi data (prinsip 12).
- Kelas harness berbeda (prinsip 13).
- Beda akun, role, atau entity (butuh login atau konteks lain), kecuali (a) spec Role Matrix (bagian 3a), atau (b) ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Kasus (b) tidak perlu dipisah, tetapi tidak boleh dipakai bila spec melewati batas ukuran atau mencampur kelas harness.
- Bergantung pada hardware atau simulasi yang berisiko (contoh: scan RFID), supaya kegagalannya tidak menutupi hasil spec lain.
- Spec yang membuat data dan butuh cleanup dipisah dari spec yang tidak membuat data, supaya kegagalan keras di spec pembuat data tidak menutupi hasil spec lain. Soft assertion tidak menolong untuk kegagalan keras (elemen tidak ketemu, modal tidak terbuka).

**Tidak boleh:**
- Menggabung TC beda akun atau role kecuali (a) ada Step khusus ganti akun, atau (b) spec Role Matrix (bagian 3a) yang langkahnya identik untuk semua role.
- Spec yang bergantung pada data atau hasil spec lain. Setiap spec bisa jalan sendiri karena suite bisa `parallel: true`, dan urutan antar spec tidak dijamin (belum diverifikasi apakah runner mengikuti nomor folder). Jadi "screening di awal" dipenuhi dengan menaruhnya sebagai langkah pertama di dalam spec.

**Batas ukuran spec** bukan jumlah langkah, tetapi apakah bagian sesudahnya masih bermakna kalau bagian sebelumnya gagal keras. Beri subjudul (`### Screening`, `### Validation`, dan seterusnya) di dalam `## Test Steps` dan sebut id TC-nya di Notes atau di langkah, supaya report per langkah bisa dipetakan ke TC.

**Alur sekali jalan:** login, buka layar, dan seed data dilakukan sekali di hook. Isi `it()` hanya berisi aksi dan assert yang benar-benar diuji.

## 3a. Role Matrix `[KEPUTUSAN 2026-09-29]`

Kasus izin per role dipisah menjadi spec **positif** dan spec **negatif** untuk tiap aksi. Satu spec dijalankan untuk banyak role, karena langkahnya identik dan hanya akun login yang berbeda. Daftar role dan akunnya ditulis di `## Prerequisites` sebagai tabel "Role yang diuji", dan langkah spec berbunyi "lakukan langkah berikut untuk setiap role pada tabel".

- **Spec positif:** aksi berhasil. Role yang diuji adalah Total Control dan role spesifik yang berhak atas aksi itu.
- **Spec negatif:** aksi tidak tersedia (Hidden atau Disabled, atau ditolak 403). Role yang diuji adalah Read Only dan role yang tidak berhak atas aksi itu.
- Kasus yang bukan soal "aksi ditolak" (sidebar tersembunyi, direct URL 403, landing state, target yang terlindungi seperti Default User dan Self) dikelompokkan sebagai spec negatif tersendiri per topik.
- **Matriks visibilitas per role** (satu daftar elemen, banyak role, hasil berbeda per role) adalah spec Role Matrix sendiri dan boleh memuat kedua polaritas (tampil dan Hidden/Disabled). Beri title tanpa kata "Positif" atau "Negatif" (contoh: "Role Matrix: Visibilitas Elemen Tab Brand per Role"); `caseType` mengikuti bagian 8.
- Kombinasi role × aksi hanya boleh ditulis kalau ada TC granular sumbernya. Kombinasi yang belum punya TC dilaporkan ke QA sebagai usulan TC baru, bukan dikarang di spec.
- Cara skrip menjalankan banyak role (perulangan di dalam satu `it()` atau beberapa kali run dengan akun berbeda) diputuskan di tahap script.
- **Susunan spec Role Matrix `[KEPUTUSAN 2026-09-29]`:** dipilih varian A, yaitu satu spec per aksi dengan positif dan negatif terpisah, karena lebih partikular. Varian B (satu spec positif dan satu spec negatif yang disusun per role, spec 021 dan 022) tidak dipakai, tetapi filenya dibiarkan untuk sementara.

## 4. Setup dan Teardown

Aturan hook TestSpectra `[VERIFIED]`: `global-hooks/*` hanya jalan saat batch run dan **dilewati saat menjalankan satu spec**. `specs/<Suite>/hooks/*` selalu jalan.

| Kebutuhan | Tempat |
|---|---|
| Health check environment | `global-hooks/before` |
| Login akun aktor sekali per suite (lewat `seedSession` atau API). Suite yang spec-nya memakai akun berbeda: login akun aktor pertama spec di hook `before` spec itu (akun dibaca dari `## Prerequisites`), dan hook `after` mengembalikan sesi ke akun default suite. Langkah login di `## Test Steps` hanya untuk ganti akun di tengah spec | `specs/<Suite>/hooks/before` |
| Reset state ringan (tutup dialog, kembali ke layar awal) | `specs/<Suite>/hooks/beforeEach` |
| Hapus data yang dibuat spec | `specs/<Suite>/hooks/afterEach` atau `after` |
| Alur bisnis berulang (buka menu, isi form) | `support/steps/<nama>/` |
| Utilitas teknis kecil | `support/actions/<nama>/` |

Hal yang tidak boleh: menaruh setup yang dibutuhkan satu spec di `global-hooks`, karena spec akan gagal saat dijalankan sendiri.

## 5. Data Uji

TC granular punya dua tabel data: **Pre-setup** (data tetap di environment, misalnya akun aktor dan user target) dan **Dinamis** (dibuat selama TC berjalan, dengan kolom Lifecycle).

- **Data Pre-setup** dirujuk lewat fixture `fixtures/<modul>.json`. Isinya identitas data, bukan rahasia.
- **Password dan token tidak boleh masuk fixture atau spec** (semua file di git). Simpan di environment variable lewat `executionConfig.environmentVariables` dan akses lewat `Spectra.env.NAMA`. `[REKOMENDASI]`, perlu keputusan tim tentang cara distribusinya.
- **Penamaan env var `[KEPUTUSAN 2026-10-08]`:** password akun aktor dipakai lintas suite dan tidak berprefix modul: `<APP>_<ROLE>_PASSWORD` (contoh `GS_TC_PASSWORD` untuk Total Control Global Settings, `AC_TC_PASSWORD` untuk Total Control Admin Console). Password uji yang dipasang ke user dinamis berprefix kode modul: `<MODUL>_PASSWORD`, varian nilai lain diberi akhiran (`_ALT`, `_72`, `_SPECIAL`), contoh `ACT_PASSWORD_72`. Input uji kebijakan yang submit-nya diblokir boleh literal. Setiap nama baru didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`, nilai dari `process.env`) dan di `.env.example`. Nilai diisi di `.env` lokal (di-ignore git) atau secret CI, lalu di-export sebelum run (contoh `set -a; . ./.env; set +a`); runner tidak terbukti membaca `.env` sendiri.
- **Data Dinamis harus unik per run.** Nilai yang harus unik (email, employee ID) dibuat dengan suffix acak atau timestamp. Kalau tidak, run kedua gagal karena data sudah ada. Suffix memuat nomor spec juga, `+{runId}-<NNN>` (contoh `budiaditya+{runId}-009@qwertysystem.net`) `[KEPUTUSAN 2026-10-08]`, supaya dua spec yang men-seed nama yang sama dari TC sumber tidak bentrok dalam satu run.
- **Lifecycle lintas TC dipecah.** Di TC granular ada data yang "dibuat di TC-A, diedit di TC-B, dihapus di TC-C". Di e2e setiap spec membuat datanya sendiri (lewat API di `before` atau `beforeEach`) dan tidak menumpang hasil spec lain.
- Data prasyarat sebisa mungkin dibuat lewat API, bukan lewat UI, supaya cepat dan tidak ikut gagal saat UI yang bukan fokus berubah.
- Data yang dibuat spec dibersihkan di `afterEach` atau `after`, dan tulis pembersihan sehingga tidak berasumsi setup berhasil penuh (aturan cascade hook).

## 6. Real Backend vs Mock

- Alur normal (happy path, validasi, permission) memakai backend asli `[REKOMENDASI]`.
- `Spectra.intercept()` untuk kondisi yang tidak bisa dipicu dengan aman di backend nyata: error 500, timeout, dan response lambat. Kasus seperti ini tetap ditulis sebagai spec, dengan `Mode: mock` dan kebutuhan mock-nya di Prerequisites.
- `Mode: mock` hanya untuk spec yang seluruh API-nya di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata) `[KEPUTUSAN 2026-10-08]`. Spec yang memaksa sebagian respons lewat `Spectra.intercept()` di atas backend nyata, atau yang mengasersi state backend (status token, status user, data di layar lain), ditandai `FE+BE` dengan kebutuhan intercept tetap ditulis di Prerequisites. Intercept hanya untuk respons HTTP yang bisa di-intercept di browser. Kegagalan di sisi server atau penyedia eksternal (flood rate-limit 429, email provider mati atau bounce, jam server digeser) tetap `FE+BE`. Pemicunya ditulis sebagai langkah eksplisit, kemampuan teknisnya tercantum di Prerequisites, dan pemulihan state (provider, jam, counter rate-limit) dilakukan di hook `after` yang tetap jalan walau spec gagal di tengah.
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
- **Bahasa spec `[KEPUTUSAN 2026-09-29]`:** `title`, heading, `## Prerequisites`, `## Test Steps`, dan `## Notes` ditulis dalam bahasa Indonesia. Teks yang tampil di aplikasi (label tombol, teks toast, tooltip, pesan error, judul dialog) ditulis persis seperti di aplikasi dan tidak diterjemahkan. Langkah asersi diawali kata `Verifikasi`. Slug pada `id` tetap bahasa Inggris supaya id tidak berubah. Spec lama yang masih berbahasa Inggris diterjemahkan sekali jalan setelah skema spec final.

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

- **Label tombol mengikuti `foundation/process/prd-process/prd-conventions.md` §24.1, bukan disalin dari TC.** Form Create: `[Submit]` dan `[Clear Field]`. Form Edit: `[Save]` dan `[Clear Field]`. Modal Create dan Edit tidak punya `[Cancel]`, dan ditutup lewat `✕` di header atau `Esc`. `[Cancel]` hanya ada di dialog konfirmasi (contoh: unsaved changes, Delete, Deactivate) dan inline Cancel pending email change. Modal Setup Column tidak punya `[Cancel]` (footer `[Reset to Default]` dan `[Save]`); dibatalkan lewat `✕` atau `Esc`.
- Semua selector hanya di Page Object. Tidak ada `Spectra.get(...)` inline di `web.test.ts`.
- Selector diutamakan `~aria-label`, lalu `#testid`. Kalau elemen belum punya, minta dev FE menambahkannya. Jangan pakai xpath atau nth-child.
- Semua teks yang diassert diambil dari fixture atau konstanta resource, bukan diketik ulang di banyak spec.
- Tidak ada komentar di kode (aturan proyek).
- `spectra lint --strict <path>` harus bersih sebelum spec dianggap selesai.

## 10. Checklist Kualitas Spec `[KEPUTUSAN 2026-10-09]`

Satu daftar aturan untuk dua pemakai: skill `tagsamurai-e2e-generate-spec` memeriksa tiap butir sebelum `spectra lint` (swa-periksa), dan skill `tagsamurai-e2e-audit` memakai butir yang sama dengan id yang sama pada kategori B, D, dan E. Audit tidak boleh menandai hal yang tidak ada di daftar ini atau di bagian lain konvensi. Kolom Tingkat adalah tingkat awal; skill audit memuat definisi tingkat.

| Id | Aturan | Tingkat |
|---|---|---|
| S-01 | Setiap butir Expected Result (a, b, c…) punya langkah `Verifikasi`. Expected bermajemuk (dua klausa atau lebih dalam satu butir) dipecah satu `Verifikasi` per klausa. Butir yang hilang adalah Berat. | Berat |
| S-02 | Teks UI (toast, dialog, placeholder, error), label tombol, dan nilai yang diketik sama persis dengan TC. Asersi tidak ditambah atau diubah maknanya tanpa dasar kolom Expected Result atau Post Condition TC. | Sedang |
| S-03 | Langkah penghubung (tutup modal atau menu, reset sort, bersihkan filter atau seleksi, pulihkan viewport) boleh, ditulis sebagai aksi tanpa awalan `Verifikasi`, dan dicatat satu butir di `## Notes`. Asersi tambahan yang tidak ada di TC tidak boleh, kecuali dicatat di `## Notes` beserta alasannya. | Ringan |
| S-04 | Langkah TC dependensi disalin utuh ke spec (atau dijalankan lewat seeding API). Dilarang menulis "mengikuti TC-xxx" sebagai pengganti langkah. Urutan aksi mengikuti TC (contoh: dialog dibuka dulu, baru pihak lain menghapus, baru konfirmasi). | Sedang |
| S-05 | Asersi "tidak ada pencatatan/log" hanya di spec absence (kelas g); spec fungsional mencatat rujukan di `## Notes`. Perubahan urutan TC di dalam spec dicatat alasannya di `## Notes`. | Sedang |
| S-06 | Spec tidak menumpang data atau hasil spec lain; seeding di `before`, cleanup di `after`. Target aksi tulis atau hapus memakai data milik spec, bukan data Pre-setup bersama. Bila terpaksa mengubah Pre-setup, pulihkan dan catat efeknya (contoh: Last Updated) di Prerequisites. | Sedang |
| S-07 | Login akun aktor pertama di hook (bagian 4); langkah login di `## Test Steps` hanya untuk ganti akun, dan ganti akun punya langkah eksplisit. Spec yang selesai di akun lain memulihkan sesi ke akun default di `after`. | Ringan |
| S-08 | Menutup form dirty ditulis deterministik: `✕`, verifikasi dialog `Unsaved Changes`, klik `[Leave]`. Reload hanya bila dialog `beforeunload` ditangani dan kemampuannya tertulis di Prerequisites. Tidak ada langkah bersyarat ("bila dialog tampil"). | Sedang |
| S-09 | State dari TC sebelumnya dalam satu spec dibersihkan sebelum TC berikutnya mengandalkannya (`Unselect All`, kosongkan filter atau Search). Pemulihan state yang diubah spec ditulis sebagai aksi tanpa `Verifikasi`, dengan hook `after` sebagai cadangan. | Sedang |
| S-10 | Urutan dalam spec mengikuti bagian 3: screening di awal, validasi diblokir sebelum aksi sukses, aksi menghapus data di akhir, jumlah buka form tidak lebih dari jumlah kejadian menutup (prinsip 6), tanpa navigasi berulang yang tidak diuji. | Ringan |
| S-11 | `## Prerequisites` memuat semua kebutuhan: akun (email dan env var), data Pre-setup dan Dinamis, nilai field wajib lain bila bagian dari objek uji, kemampuan teknis, state global beserta pemulihannya, dan `Mode`. Isinya sama dengan yang dipakai langkah (tidak ada data yang tidak dipakai, tidak ada yang kurang). Notes bukan satu-satunya tempat sebuah kebutuhan. | Sedang |
| S-12 | Data Dinamis bersuffix per run (pengecualian: Population D-01, 12 brand `Apex Tools` … `Linear Dynamics`, bernama literal karena asersi urutan A-Z dan jumlah; di-seed idempotent, yaitu dilewati bila sudah ada, dan cleanup hanya menghapus yang dibuat spec itu; spec yang menghapus atau mengubah brand memakai brand milik sendiri bersuffix; suite berjalan serial); nama hasil rename atau perubahan ditulis (seeding dan cleanup deterministik); password dan token hanya lewat env; fixture yang belum ada ditandai di Prerequisites. | Sedang |
| S-13 | Tidak mengarang endpoint, akun, atau mekanisme yang tidak ada di TC, PRD, atau LLD (contoh: endpoint untuk persistensi UI yang PRD sebut `localStorage`). Kebutuhan mock hanya untuk endpoint yang tercantum di sumber. | Sedang |
| S-14 | Asersi yang bergantung posisi atau keadaan memuat langkah menuju keadaannya (pindah ke halaman terakhir sebelum "di akhir", placeholder dicek saat input kosong, kolom di-hide sebelum dicek hilang). | Sedang |
| S-15 | Bila TC sumber ambigu, kontradiktif, atau kurang precondition, spec tetap mengikuti TC dan masalahnya dicatat di `## Notes` (butir "Temuan untuk QA") serta di laporan akhir generate. Menambal diam-diam tanpa catatan adalah temuan. | Sedang |

