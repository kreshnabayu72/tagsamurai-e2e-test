---
name: Global Settings All Tags
id: suite-global-settings-all-tags
description: Spec e2e turunan tc-all-tags.md untuk Global Settings > All Tags
executionOrder: 1.8
parallel: false
---

# Suite: Global Settings All Tags

Suite ini mencakup halaman All Tags pada Global Settings: registri TAG (tiga tab All, Paired, Not Paired; isi sel, kartu counter, Search, Search by Scan, Filter, Sort, Pagination, Setup Column, Download CSV/XLSX), Activate TAG (Select TAG Type, halaman Activate, Template Self-Purchased, pencocokan staging, unggah GPS, Row Edit Mode, Bulk Resolve, Remove, Submit Activation), Audit TAG, Delete TAG (single, bulk, Delete by Scan, Selection Limit), modal Event Log dan popup Detail, popup TAG Log, pencatatan log di tiga surface (Event Log, Activity Log, System Log aktor), atribusi hardware, Guided Tooltip, Role Matrix per capability Manage TAG, plan tier dan state tenant, sinkronisasi lintas modul (Fixed Asset/FAMS, Approvals, Supply Asset, Admin Console, katalog), request langsung dan isolasi Client, serta ketahanan terhadap kegagalan server. Spec dibagi dalam enam kelompok nomor: 001-015 (registri, akses, plan, tenant, keamanan, mobile), 016-029 (Activate sebelum Submit), 030-045 (Activate commit dan Audit), 046-065 (Delete dan sinkronisasi lintas modul), 066-081 (aturan tabel registri), 082-101 (Event Log, pencatatan, TAG Log, format tanggal; 098-099 lanjutan Delete lintas FAMS, 100-101 Setup Column surface mock).

`parallel: false` karena spec mengubah state global dan menghapus data (lihat daftar di bagian "State global yang dipulihkan"). Identifier TAG (EPC, IMEI, UID) bersifat tetap dan tidak bisa diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: tiap spec mengembalikan dataset yang dipakainya ke kondisi awal lewat hook `before` sebelum aksi pertama dan tidak bergantung pada hasil spec lain. Hitungan tetap (30 baris Seed Registri A, 26 baris Not Paired, kartu `21 of 50`, `Showing ... of 30`) valid hanya bila suite berjalan serial dan dataset di-seed ulang per spec. Kumpulan Event Log dan Activity Log menumpuk antar spec dan tidak dibersihkan, sehingga hitungan entri log tidak diasersi sebagai total absolut: spec memakai baseline jumlah entri sebelum aksi atau identifier uji yang unik. Spec yang menghapus data (Delete single, Bulk Delete, Delete by Scan) dan spec yang mengubah state global menaruh aksi destruktif di akhir spec; urutan antar spec mengikuti nomor, tetapi belum terbukti dijamin runner.

## Hook Guided Tooltip

Hook `before` suite menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi `true` untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat), agar walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal. Mekanisme penyetelan flag disediakan tim FE/BE. Pengecualian: spec 005 (Guided Tooltip registri) mengatur flag `gs-tag-registry` sendiri dan spec 037 (Guided Tooltip halaman Activate) mengatur flag `gs-tag-activate` sendiri; keduanya menulis pengaturan flag di `## Prerequisites` masing-masing. Tiap spec lain memuat satu baris rujukan ke pernyataan ini di `## Prerequisites`.

## State global yang dipulihkan hook `after`

- Plan tier Client (Free, Growth, Professional, Enterprise), status Client (Active, Suspended, Expired), dan opsi mandiri (BYO) Client A serta Client Quota.
- Ukuran halaman tabel registri (Rows per page) dikembalikan ke 10 oleh spec yang mengubahnya (002, 046, 050-053, 056-061, 081, 083, 098 dan lainnya yang menulis langkah Rows per page).
- General Settings: format tanggal/waktu dan timezone.
- Admin Console: Communication Endpoint (Domain dan IP Address Info Box GPS), kuota/alokasi TAG Stock, katalog (Brand, Device Name, SKU), Selection Limit dan Master Data Count Limit.
- Capability role/akun (Manage TAG, Manage asset & TAG) yang dicabut atau diubah untuk spec Role Matrix dan konflik.
- Jam server dan jam browser/klien bila spec mengaturnya (Last Scanned, batas waktu).
- Flag Guided Tooltip (lihat di atas).
- Seed Registri A (DD-01..DD-30), fixture khusus DD-60..DD-63 (spec 002 dan 058), stok resmi DD-S1..S10, identifier uji DD-N1..N13, Seed Client Audit, fixture TAG Log, fixture Event Log, dan tag Client Large: dikembalikan ke kondisi awal secara idempotent oleh hook `before` spec yang memakainya dan oleh hook `after` spec yang mengubahnya.

## Kemampuan teknis yang dibutuhkan (disediakan tim FE/BE)

Mekanisme dan endpoint tidak didefinisikan di TC, PRD, maupun LLD yang dibaca tahap ini; spec menulisnya sebagai kemampuan dan tahap script wajib melengkapinya dari `openapi.yaml` (S-13).

- Seed dan reset idempotent registri, stok, identifier uji, Client Audit, fixture log, dan client uji per spec (Q-4).
- Simulasi reader RFID/NFC/BLE (scan, putus, timeout, Handheld Reader `Zebra RFD40 (SN-2201)`) untuk spec kelas hardware (D-4, Q-1).
- Entri manual GPS dan unggah berkas CSV/XLSX/pdf uji.
- Intercept jaringan (500, timeout) di atas backend nyata.
- Sesi API admin kedua (Admin B) sebagai pemicu: pair/unpair/dispose/replace/retire dari FAMS, approve/reject di Approvals, ubah kuota, katalog, Communication Endpoint, plan, status Client, capability, format tanggal, dan timezone di Admin Console dan General Settings  (Q-5).
- Pembaca berkas unduhan CSV/XLSX; penanganan dialog `beforeunload`.
- Android emulator atau perangkat untuk spec mobile (015).
- Klien HTTP untuk request langsung ke server (spec 014) dan dua konteks browser atau sesi API.
- Pengaturan jam server dan jam browser bersama (Last Scanned, Q-6).

## Mode

Spec 075, 077, 085, 100, dan 101 berstatus `Mode: mock` (Setup Column screening, pin, reset, dan surface sekunder; keputusan D-3, pola File Manager). Semua spec lain `Mode: FE+BE` (spec 015 FE+BE mobile).

## Kredensial

Password aktor lewat `Spectra.env`, satu nama env satu arti. Sudah terdaftar di `.env.example`: `GS_TC_PASSWORD` (Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, sesuai Pre-setup TC; akun `totalControlGlobalSettings_automated_{namaCompany}` milik suite lain), `GS_RO_PASSWORD` (Read Only), `GS_NOCAP_PASSWORD` (tanpa capability TAG), `GS_TC2_PASSWORD` (Total Control kedua), `FA_ADMIN_PASSWORD` (FAMS Admin), `GS_CLIENTB_TC_PASSWORD` (Total Control Client B), `GS_PRINCIPAL_TC_PASSWORD` (Principal approver), `GS_LIMIT_TC_PASSWORD` (Client Limit), `GS_TC_EMPTY_PASSWORD` (client tanpa data).

Belum terdaftar dan perlu didaftarkan pemilik repositori di `spectra.config.ts` dan `.env.example` (tanpa nilai; penamaan `<APP>_<ROLE>_PASSWORD`): `GS_TAG_UPDATE_PASSWORD` (Manage TAG: Update), `GS_TAG_READ_PASSWORD` (Manage TAG: Read), `GS_FAMS_ASSETTAG_READ_PASSWORD` dan `GS_FAMS_ASSETTAG_UPDATE_PASSWORD` (Manage asset & TAG di FAMS: Read dan Update), serta Total Control per client uji: `GS_TC_ALLPAIRED_PASSWORD`, `GS_TC_FREE_PASSWORD`, `GS_TC_DOWN_PASSWORD`, `GS_TC_NOBYO_PASSWORD`, `GS_TC_QUOTA_PASSWORD`, `GS_TC_OVER_PASSWORD`, `GS_TC_SUSP_PASSWORD`, `GS_TC_AUDIT_PASSWORD`, `GS_TC_LOG_PASSWORD`, `GS_TC_LARGE_PASSWORD`, `GS_TC_PROFESSIONAL_PASSWORD`, `GS_TC_ENTERPRISE_PASSWORD`. Akun Admin Console (alokasi kuota, katalog, Communication Endpoint) tidak ada di Pre-setup TC dan ditulis "disediakan tim FE" (S-13).

## Sesi API aktor

Spec yang memakai pelaku kedua lewat sesi API (login API dengan password, token tidak dihitung sebagai sesi web sehingga sesi UI tidak diusir) merujuk bagian ini dengan satu baris di `## Prerequisites`. Kemampuan itu disediakan tim BE/FE. Spec yang memakainya: 012, 013, 018, 027, 032, 033, 034, 036, 039, 044, 052, 053, 056, 057, 058, 059, 060, 061, 063, 064, 065, 087, 096.

## Spec yang menyimpan konfigurasi kolom

Hook `after` spec berikut memulihkan konfigurasi kolom Setup Column dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`: 002, 031, 067, 068, 069, 070, 074, 076, 077, 078, 085, 096 (Last User), 097 (Activated At), 100, 101. Spec 075 tidak menyimpan konfigurasi tetapi hook `after`-nya memulihkan dengan cara yang sama.

## Asumsi tanggal lingkungan

Spec yang memakai Filter Date pada Event Log (082, 083, 086, 097) mengandalkan tanggal sistem saat run lebih besar dari 16/09/26 dan tidak ada spec yang memundurkan jam ke rentang seed 07/08/26 sampai 16/09/26. Rentang yang dipakai tiap spec tertulis di `## Prerequisites` spec itu.

## Legenda keputusan dan pertanyaan

Id `D-n` dan `Q-n` di `## Prerequisites` dan `## Notes` spec mengacu ke daftar berikut.

- **D-1:** klausa absence log ditulis di spec asal dengan baseline jumlah entri sebelum aksi, tanpa spec absence tambahan.
- **D-2:** TC request langsung ke server tetap di E2E sebagai satu spec defense-in-depth (spec 014); asersi hanya status respons dan state data.
- **D-3:** Setup Column screening, pin, reset, dan surface sekunder berjalan `Mode: mock`.
- **D-4:** TC yang butuh scan hardware tetap masuk spec sebagai kelas d dengan simulasi reader yang disediakan tim FE.
- **D-5:** TC-32 di spec Audit dan TC-175 di spec sendiri, bukan di spec Role Matrix atau plan.
- **Q-1:** cara simulasi reader RFID/NFC/BLE tidak didefinisikan di sumber.
- **Q-2:** akun Pre-setup TC (`totalControl2_automated_qaTeam1`, `principalApprover_automated`) perlu dikonfirmasi tim FE terhadap `.env.example` saat tahap script.
- **Q-3:** nilai literal Domain dan IP Address Info Box GPS tidak ditetapkan di TC.
- **Q-4:** identifier tetap tanpa sufiks per run; hitungan tetap valid hanya dengan reset fixture BE per spec.
- **Q-5:** pemicu "tepat saat commit" ditulis sebagai fixture BE lewat sesi API.
- **Q-6:** Last Scanned dan jeda satu menit diatur lewat jam server dan browser, bukan menunggu.
- **Q-7:** nilai Selection Limit `L` tidak diberi angka di TC.
- **Q-8:** Expected TC-292, 318, 321, 328 terlalu umum; spec mengikuti TC dan mencatat di Temuan untuk QA.
- **Q-9:** langkah dan selektor modul konsumen (FAMS, Approvals, Admin Console, Supply Asset) disediakan tim FE.
- **Q-10:** TC-321 tidak menyebut modul dan copy penolakan.
- **Q-11:** viewport untuk scroll horizontal Setup Column tidak ditetapkan di TC.
- **Q-12:** timezone target TC-312 dan pemulihan state global TC-309 ditetapkan tim FE.
- **Q-13:** metadata VAL turunan dari Tabel Data Uji (informasional).
- **Q-14:** penempatan topik TC-13, 21, 168 menurut topik aksi (informasional).
- **Q-15:** pelaku TAG Log hanya tersedia sebagai fixture Client Log; akun pelaku disediakan tim FE.
