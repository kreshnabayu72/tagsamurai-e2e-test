---
name: Admin Console Client
id: suite-admin-console-client
description: Spec e2e turunan tc-client.md untuk Admin Console > Client
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Client

Suite ini mencakup halaman Admin Console > Client: List Client (tiga sub-tab Active, Suspended, Archived, kolom, Search, Filter, Sort, Pagination, Setup Column, Download, Select Group tree, bulk select dan Select All), popup New Client dan Edit Client, Change Partner, Suspend, Unsuspend, dan Delete (termasuk bulk), Detail Client (header, Tab Subscription, Tab Asset Control, tab Tag, Storage, dan Hardware, tabel Purchase History, Quota, serta modal Changelog), Role Matrix dan scope Group per aktor, pencatatan di Changelog, Activity Log, dan System Log, aksi sistem terjadwal (Auto-Archive, Purge, Renewal, Auto-Reactivate), notifikasi dan Activation Email, sinkronisasi SSE, tampilan Android native, serta ketahanan terhadap kegagalan server.

`parallel: false` karena modul ini memakai state global bersama: jam server (job lifecycle), Selection Limit (System Limits), flag Guided Tooltip akun aktor, Date Format General Settings, permission role, dan fixture Tabel A3 yang dikonsumsi atau dipulihkan spec. Select All, Bulk Delete, dan Bulk Suspend juga memengaruhi populasi List yang dibaca spec lain. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

Hook berikut dinyatakan sekali di sini; `## Prerequisites` tiap spec merujuknya dengan satu baris. Implementasi hook dibuat tim FE pada tahap script. Kemampuan teknis yang tidak didefinisikan di TC, PRD, atau LLD ditulis "disediakan tim FE/BE" tanpa endpoint karangan (S-13).

### before

- Health check environment ada di `global-hooks/before`, bukan di sini.
- Login akun aktor pertama spec (akun dibaca dari `## Prerequisites` spec; akun default suite adalah Total Control Principal A-01, `AC_TC_PASSWORD`). Login untuk ganti akun di tengah spec ditulis eksplisit di `## Test Steps`.
- Menyetel flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` ke true untuk akun aktor yang dipakai spec (agar tooltip tidak menutupi halaman). Spec yang menguji flag itu sendiri (spec 020, 021, 022, 023) menulis pengecualiannya di Prerequisites dan mengaturnya sesudah hook. Mekanisme menyetel flag disediakan tim FE/BE.
- Seeding ulang fixture Tabel A3 yang dikonsumsi atau diubah spec, lewat Fixture BE yang idempotent (dilewati bila sudah ada dan dalam keadaan awal), disediakan tim FE/BE. Contoh yang dinyatakan di Prerequisites spec: C-LIF-12 `PT Suspend Tanpa Produk`, C-FX14-1 `PT Suspend Arsip Reaktivasi`, C-04, C-09, C-FX14-2, serta fixture C-AST, C-DTL, C-LIF, dan C-ROL lain. Spec yang menulis data memakai salinan bersuffix `{runId}-NNN` milik sendiri (S-06, S-12); mekanisme seeding salinan fixture A3 disediakan tim FE/BE.
- Pengecualian S-12 yang diizinkan pemilik (keputusan 2026-11-02): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix untuk asersi urutan A-Z, jumlah, badge, dan isi sel; syaratnya seeding idempotent, suite serial, dan spec tidak menjadikan Client literal itu target aksi tulis kecuali Prerequisites menyatakan pemulihannya.

### beforeEach

- Membuka Admin Console > Client (List). Klik sidebar mereset Search, Sort, dan Filter; state yang harus dipulihkan ditulis sebagai langkah pemulihan eksplisit di spec.
- Menutup dialog atau popup sisa dan kembali ke layar awal. Reset state ringan saja; tidak ada seeding data di hook ini.
- Pengecualian spec 020, 021, 022, 023 (Guided Tooltip): hook `beforeEach` tidak membuka List Client dan membuka halaman netral (mis. Dashboard), supaya kunjungan pertama ke List atau Detail Client menjadi langkah 1 spec dan tidak terpakai sebelum langkah itu. Kemampuan hook yang dapat dikecualikan per spec disediakan tim FE.

### afterEach

- Menghapus data Dinamis yang dibuat spec (Client, Partner, Group sementara bersuffix) lewat API tanpa mengandaikan setup berhasil penuh. Dasar: bagian 5 konvensi.

### after

- Mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`) bila spec selesai di akun lain (S-07).
- Memulihkan flag Guided Tooltip akun aktor ke nilai awal.
- Menghapus preferensi kolom Setup Column di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE, bagian 4 konvensi) untuk spec yang menyimpan konfigurasi kolom (List Client, tabel sekunder Detail seperti Station List, dan ketiga modal Changelog): spec 052, 215, 245, 256, 257, 258, 259, 260, 282, 293, 294, 295, 296, 297, 298, 299, 300; tiap spec menyebut tabel yang disimpannya di Prerequisites.
- Memulihkan jam server dan jam browser ke waktu nyata (spec yang memanipulasi jam: 079, 080, 081, 128, 142, 145, 221, 222, 223, 232, 234, 235, 236, 238, 246, 247, 270, 313, 314) dan Selection Limit ke default 1000 (spec 140, 306; Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits).
- Memulihkan Date Format General Settings ke `dd/MM/yy` (spec 321) dan permission role yang diubah spec (spec 153).
- Membatalkan simulasi kegagalan (email service, Global Settings tidak terjangkau, intercept yang tersisa) dan memulihkan fixture A3 yang dikonsumsi lewat seeding ulang.
- Menutup konteks browser kedua atau tab kedua yang dibuka spec.

## Kemampuan teknis yang disediakan tim FE/BE

- **Sesi API aktor:** login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir dan batas satu sesi web tidak terpengaruh (bagian 5 konvensi). Dipakai sebagai pelaku kedua yang hanya memicu perubahan state dan klien HTTP untuk request langsung ke server (kelas defense-in-depth). Spec merujuk ke bagian ini dengan satu baris.
- **Fixture BE:** seeding, seeding ulang, dan penghapusan Client, Partner, Group, dan pengguna; pembacaan state yang tidak terlihat di UI hanya untuk butir Expected TC.
- **Sesi tetap valid saat jam digeser:** sesi UI dan sesi API aktor tetap valid selama jam server dan jam browser digeser, sehingga spec yang memajukan jam tidak kehilangan login (dipakai spec 079, 080, 081, 128, 142, 145, 221, 222, 223, 232, 234, 235, 236, 238, 246, 247, 270, 313, 314). Spec itu merujuk butir ini dengan satu baris di `## Prerequisites`. Disediakan tim FE/BE.
- **Dua sesi web akun yang sama:** spec dua sesi (146, 151, 224) memakai Sesi B dengan akun yang sama (atau akun kedua setara yang disediakan) tanpa mengusir Sesi A; batas satu sesi web dilonggarkan untuk akun uji (bagian 5 konvensi). Disediakan tim FE/BE.
- **Jam server dan jam browser:** diatur absolut atau dimajukan untuk job lifecycle dan batas waktu; keduanya diatur bersama kecuali spec menyatakan hanya jam server (bagian 6 konvensi), dan dipulihkan sebelum Activity Log atau Changelog dibuka.
- **Mail-catcher:** membaca inbox Default User dengan baseline jumlah email sebelum aksi.
- **Intercept dan pemaksaan kegagalan:** respons 5xx per jenis request, penahanan respons, kegagalan email service, dan Global Settings tidak terjangkau.
- **Simulator reader, tablet, atau SFR Asset Control**, perangkat Android native, dan pengubah ukuran viewport.
- **Env var password aktor:** nama dan pemetaan kanonik ada di `docs/coverage/AdminConsoleClient.md`; sudah terdaftar di `spectra.config.ts` dan `.env.example` (semua nama `AC_CLIENT_*_PASSWORD` beserta `AC_TC_PASSWORD`).
