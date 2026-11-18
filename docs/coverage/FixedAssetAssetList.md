<!-- Ditulis stage spec-from-prd saat close. Jangan diubah tangan: run berikutnya menimpanya. -->

Suite: `specs/FixedAsset/AssetList`. Sumber: PRD `fixed-asset@f688ea9` (sha `71e4f6b3cc546171`), foundation@96df7b2, kontrak komponen wangs-ui@1.0.0. Stage: `prd-harness@63da747`, ditutup 2026-11-18T05:28:48Z.
Plan, unit PRD, data, dan vonis per unit: `docs/spec-from-prd/FixedAssetAssetList/`.
# Audit Asset List

- Putaran: 2. Unit dinilai: 952 (ok 717, parsial 20, hilang 0, salah 0, na 215).
- Skor: 98.6% (ok + setengah parsial, dibagi unit berperilaku).
- Spec `ready-for-automation`: 92. Spec tetap `draft`: 0.

## Keputusan pemilik PRD (39)

Hanya bagian ini yang butuh manusia: sumber bertentangan atau belum memutuskan. Keputusannya ditulis di PRD, lalu spec yang ditahan dibuat.

- Temuan 1 (kurang): PRD tidak menyatakan hasil saat opsi yang sedang dipakai sebagai kriteria Filter dihapus aktor lain; EB-FLT-7 ditahan sampai PRD menetapkannya Unit ditahan: `EB-FLT-7`.
- Temuan 4 (bertentangan): EC-45 dan indeks State S-27 masih memakai bunyi lama (Disabled menurut Custody selain Available); yang diasersi mengikuti Matriks Aksi dan tabel S-27: Report Missing aktif untuk Custody apa pun, Disabled dengan S-27 hanya untuk baris Transfer In Transit
- Juri, unit `FLD-11`: Aturan bahwa selama aset Assigned field Division diisi Division Assignee dan dikembalikan saat Unassign (kolom menampilkan nilai itu) ditetapkan `assignment.md` ASSIGN-LOGIC-06, di luar kit; tidak dihitung kurang.
- Juri, unit `§4.2.1#p1`: Tab Registration/Damaged/Missing 'menurut hak akses' modul pemilik (asset-registration/, damaged/, missing/) ditetapkan di luar kit; tidak dihitung kurang.
- Juri, unit `§4.8#p1`: Visibilitas tab Registration/Damaged/Missing 'menurut hak modul pemiliknya' (asset-registration/, damaged/, missing/) ditetapkan dokumen di luar kit; suite hanya mengasersi keempat tab tampil bagi Total Control (E2E-001 langkah 3). Tidak dihitung kurang.
- Juri, unit `§9.2#p2`: PRD 9.2 [F-ASTL-02]: "Jumlah kartu `Available` selalu sama dengan jumlah baris sub-menu `available/` bila filter lain kosong." Sub-menu `available/` adalah surface/modul lain di luar kit; E2E-002 langkah 20 hanya membandingkan kartu Available dengan total tabel kartu itu, bukan dengan sub-menu `available/`. Tidak dihitung kurang.
- Juri, unit `ASTL-LOGIC-18`: Klausa 'konteks daftar dibawa sebagai parameter URL; server menghitung aset sebelum dan sesudahnya' (hasil tampilnya, navigasi sebelum/sesudah) dimiliki `asset-detail.md` §4.1d, di luar kit; suite ini hanya bisa mengasersi pembukaan dari kolom Name dan pemulihan state daftar.
- Juri, unit `ASTL-LOGIC-15o`: Klausa 'dihitung Used' sesudah jeda transisi adalah surface modul `license/` (Used/Reserved) yang ditetapkan di luar kit; tidak dihitung kurang.
- Juri, unit `ASTL-LOGIC-17a`: Penanda ⚠ pada baris aset terhapus di Draft Borrow/Transfer/Assignment (EC-41) dan hitung ulang agregat record dimiliki modul transaksi/pemilik record; tidak dihitung kurang (BE-087 langkah 43 hanya asersi draft tidak disentuh).
- Juri, unit `§9.7#r14`: 'asset-detail/: data aset tidak lagi tersedia' adalah surface modul Asset Detail; tidak dapat diasersi suite ini, tidak mengubah verdict.
- Juri, unit `ASTL-LOGIC-21e`: Klausa 'aset tidak masuk Depreciation Run (Open Item #19)' ditetapkan modul Depreciation Run/Open Item #19, di luar kit; tidak dihitung kurang.
- Juri, unit `EC-40`: Klausa 'aset tidak masuk Depreciation Run (Open Item #19)' ditetapkan modul Depreciation Run/Open Item #19, di luar kit; tidak dihitung kurang.
- Juri, unit `§9.7#r13`: 'Tab Purchasing dan Book value di asset-detail/' adalah surface modul Asset Detail; tidak diasersi suite ini.
- Juri, unit `ASTL-LOGIC-20j`: 'Kelayakan aset dievaluasi ulang di form saat dikirim, salinan penolakan dimiliki modul transaksi' ditetapkan modul Borrow/Assignment/Transfer di luar kit; tidak dihitung kurang.
- Juri, unit `AddtoTransferDraft`: Hasil Add to Transfer Draft (dialog T-XFER-02, 'aset tidak dikunci sampai Submit', transfer.md) dan kelayakan Custody (asset-state-machine.md §5) dimiliki dokumen/modul di luar kit; tidak diasersi.
- Juri, unit `Detail`: Eksekusi 'Asset Detail' dari Row Action Detail adalah surface modul Asset Detail; klik Detail tidak dijalankan di suite (navigasi hanya lewat kolom Name, E2E-010), tidak dihitung kurang.
- Juri, unit `EC-45`: PRD tidak konsisten: EC-45 (§9.4.2) 'Report Missing pada aset dengan Custody selain `Available` ... Aksi `Disabled 🔖` ... tooltip `S-27` menurut Custody' vs Matriks Aksi §4.1b Report Missing: 'Custody apa pun kecuali `In Transfer Process` dengan baris Transfer `In Transit`' dan `Disabled 🔖` S-27 'hanya bila baris Transfer aset `In Transit`' (S-27 juga khusus Transfer In Transit). Tidak ada aturan penentu sisi; suite mengikuti Matriks (aktif pada Borrowed/Assigned, Disabled hanya In Transit).
- Juri, unit `EC-46`: Hasil laporan di damaged/ atau missing/ (Condition master berubah seketika walau Require approval Audit aktif; Work Order, jadwal maintenance, item sesi Stock Opname tidak berubah; DAMAGED-LOGIC-03p, MISS-LOGIC-04i/04j) dimiliki modul Damaged/Missing/Audit/Maintenance; tidak dihitung kurang. Aksi tetap aktif pada In Audit (langkah 27) dan Under Maintenance (langkah 95) sudah diasersi.
- Juri, unit `MarkasReturned`: Kolom Activity Lock dan hasil dialog D-BRW-25 mengikuti borrow.md §9.11 (di luar kit); tidak diasersi.
- Juri, unit `MarkasUnassigned`: Kolom Activity Lock dan hasil dialog D-ASG-26 mengikuti assignment.md §9.10 (di luar kit); tidak diasersi.
- Juri, unit `ReportDisposal`: Pembuatan Disposal Report lewat `D-DISP-13` dan kelayakan `DISP-LOGIC-15` dimiliki `disposal.md` (di luar kit).
- Juri, unit `ReportMissing`: EC-45 'Report Missing pada aset dengan Custody selain Available: Disabled dengan tooltip S-27' dan S-27 di indeks (baris 1333) 'karena Custody aset selain Available' bertentangan dengan Matriks Aksi 'Custody apa pun kecuali In Transfer Process dengan baris Transfer In Transit' dan S-27 §7 'hanya bila baris Transfer In Transit'. Suite mengikuti Matriks. Efek ke transaksi berjalan dimiliki borrow/assignment/transfer.md.
- Juri, unit `Transfer`: Kelayakan Custody (asset-state-machine.md §5) dan perilaku Transfer pada level None (transfer.md §9.11) berada di dokumen di luar kit; tidak diasersi.
- Juri, unit `§9.11#r1`: Transaction Log adalah surface Asset Detail (asset-detail.md), di luar kit; hasil cakupannya tidak bisa dipastikan suite ini.
- Juri, unit `§9.11#r3`: 'Purchase Information' pada Asset Detail dimiliki `asset-detail.md` (seksi Purchase & Value); tidak diasersi di suite, tidak dihitung kurang.
- Juri, unit `§9.10#p2`: PRD §9.10: 'serta `Transfer` dan `Add to Transfer Draft` sesuai modulnya' pada level None merujuk `transfer.md` §9.11 (di luar kit); keadaan Transfer pada level None tidak diasersi (Add to Transfer Draft Hidden pada None sesuai 'Draft hanya di level Full').
- Juri, unit `§8#b4`: Klausa 'Aksi Asset Detail: asset-detail.md §8' menunjuk dokumen modul lain; pencatatan aksi Asset Detail di Activity Log tidak dapat diasersi suite ini (PRD asset-detail.md).
- Juri, unit `§8#b5`: Pencatatan pelepasan TAG ke To Be Returned dan pengeluaran baris dari record multi-aset dimiliki modul tag/ dan modul pemilik record (PRD baris 1554); hasil di sana tidak bisa diasersi suite ini.
- Juri, unit `ASTL-LOGIC-11d`: Klausa menyebut Maintenance sebagai modul lain yang menampilkan garansi dengan nilai dan hover sama; surface modul Maintenance milik modul lain dan tidak ada spec dep-maintenance. Tidak dihitung kurang.
- Juri, unit `ASTL-LOGIC-16c`: ASTL-LOGIC-16c 'TAG yang sudah Paired tetap terpasang sampai aset dihapus (Delete Asset Data) atau didisposal' tidak menetapkan apakah disposal melepas TAG; DU-046-2 (Disposed masih ber-TAG Paired) dan ASTL-LOGIC-17x (lepas lewat To Be Returned saat Delete) tidak memutuskan sisi mana.
- Juri, unit `S-27`: S-27 'Dirujuk juga oleh damaged.md' dan alur Lost in Transit (`transfer.md` XFER-LOGIC-16) dimiliki modul lain; tidak diasersi suite ini.
- Juri, unit `S-35`: ID S-35 dipakai ganda di PRD §7: baris 1478 'Tooltip aksi Report Disposal yang Disabled karena Custody selain Available' dan baris 1480 'Tooltip info di samping label Document No. pada D-13'. Suite mengasersi keduanya (UI-061 langkah 134-153; UI-071 langkah 8).
- Juri, unit `§4.2.1#p2`: Breadcrumb tab `Registration`, `Damaged`, `Missing` dimiliki `asset-registration/`, `damaged/`, `missing/` dan Breadcrumb Asset Detail dimiliki `asset-detail.md` §4.2.2 (PRD baris 715); tidak bisa diasersi suite ini.
- Juri, unit `§4.1i#p1`: Pintu masuk menu ⋮ Asset Detail dan tombol `Edit Purchase` di tab Purchasing (hanya bagi aktornya) ada di surface `asset-detail.md` (§4.1d), tidak dapat diasersi suite ini; hasilnya ditetapkan dokumen itu.
- Juri, unit `§9.9#r11`: Pesan batas dan format custom field 'menurut settings-custom-fields/' (modul lain); literalnya tidak ditetapkan di PRD ini sehingga tidak bisa diasersi suite ini.
- Juri, unit `F-ASTL-16.k4`: Nilai Managed Action Retry Delay dan jeda dimiliki 'plans-licensing-lifecycle-settings/' ('n/a — nilai jeda dimiliki plans-licensing-lifecycle-settings/'); suite ini tidak bisa menetapkan nilainya, jadi hanya perilaku jeda (EC-49) yang diasersi.
- Juri, unit `EC-33`: EC-33: 'aksi transaksi: dievaluasi ulang di modul transaksi (ASTL-LOGIC-20)'; hasil ditetapkan PRD modul transaksi (Borrow/Assign/Transfer), tidak bisa diasersi suite ini; tidak mengubah verdict.
- Juri, unit `ASTL-LOGIC-10a`: ASTL-LOGIC-10a: 'pada Asset Detail berlaku untuk seksi Purchase & Value' adalah surface modul asset-detail (asset-detail.md); tidak diasersi suite ini dan tidak mengubah verdict.
- Juri, unit `EB-FLT-7`: PRD hanya menetapkan hasil untuk rujukan terhapus pada filter/konfigurasi TERSIMPAN saat dimuat (EC-43: 'Setup Column atau filter tersimpan merujuk custom field, label, atau Category yang sudah dihapus -> dibuang diam-diam', juga §5 Setup Column); itu diasersi UI-059 langkah 74-78. Hasil saat opsi yang sedang dipakai di panel Filter aktif dihapus aktor lain, dan untuk jenis opsi lain (Group, Asset Class, Status, Brand dll), tidak ditetapkan PRD.

## Drift antar-sumber (4)

Tempat PRD berbeda bunyi dengan foundation atau dengan kontrak komponen. Spec tidak menunggu apa pun: aturan stage sudah menetapkan sisi yang diasersi (foundation untuk pola bersama, kontrak komponen untuk mekanik komponen). Daftar ini menunjukkan bagian mana yang berlawanan dan dokumen mana yang perlu diperbaiki.

- Planner, temuan 2 (beda-foundation): Setup Column adalah pola bersama; yang diasersi mengikuti foundation (SB-4): konfigurasi tersimpan di akun user, bukan hanya di browser
- Juri, unit `FLD-06`: Kontrak DataTable#6: 'an empty (null/undefined) value goes last in both directions'; foundation prd-conventions §9.15: nilai kosong 'di akhir saat ascending dan di awal saat descending'. Spec mengasersi versi foundation (baris tanpa Brand paling awal saat descending) tanpa footnote drift. Unit tidak memuat `kontrak` dan tabel ini server-driven (DataTable#8), sehingga sisi yang berlaku dinilai foundation dan verdict tidak berubah; mohon konfirmasi untuk semua kolom sortable.
- Juri, unit `FLD-12`: Foundation (Setup Column +N more / §21): chip membuka popover; kontrak BadgeGroup#4: `+N more` membuka modal dialog berjudul `All Items`. Sisi yang berlaku: kontrak komponen untuk mekanik; spec menyebut 'popover' tanpa footnote drift.
- Juri, unit `§5#r8`: PRD §5 Setup Column: 'Disimpan di browser per user'; foundation §9.3/EB-KOL-2: 'tersimpan per user di akun' (bertahan di browser lain). Sisi yang berlaku: foundation (pola bersama). E2E-007 mengasersi sisi foundation (sesi browser terpisah, langkah 28-30) tanpa footnote `[^drift-n]`.

## Unit yang belum teruji penuh (20)

Spec yang memuatnya benar, tetapi klausa di bawah belum diasersi. Ini yang menurunkan skor.

- unit `FLD-22` (parsial; kurang; langkah 117, 118): PRD baris Warranty Expiry: sort 'No access selalu paling akhir' (ASTL-LOGIC-10q, kedua arah). Aktor E2E-005 (Total Control) tidak punya sel `No access`, dan BE-090 langkah 11-14 hanya mengasersi urutan Purchase Cost. Perlu aktor tanpa hak Purchase yang mengurutkan Warranty Expiry asc dan desc dan melihat `No access` paling akhir (idealnya di BE-090).
- unit `FLD-23` (parsial; kurang; langkah 121, 122): Sort custom field 'menurut Data Type: numerik, tanggal, atau A-Z' hanya diuji untuk tipe teks (`Lokasi Rak`). Tambah custom field numerik dan tanggal dan verifikasi urutan numerik/kronologis.
- unit `FLD-23` (parsial; kurang; langkah 7): Kapabilitas Filter/Search per Data Type (PRD baris Custom field: Dropdown/Multi-Dropdown multi-select dengan opsi = nilai distinct, Date rentang, Numeric/Percentage/Currency Min/Max, Text hanya Search, Document tanpa keduanya) hanya diuji untuk tipe teks (tanpa field filter). Tipe lain tidak diuji.
- unit `ASTL-LOGIC-14n` (parsial; kurang; langkah 35, 36, 37, 38, 39): Klausa kedua: kembali ke `All Groups` karena node aktif keluar cakupan (14f) memuat ulang tabel dari halaman 1 dengan seleksi baris bertahan. Tidak ada asersi halaman 1 aktif dan seleksi baris bertahan sesudah pengembalian otomatis (E2E-034 langkah 6 hanya node kembali ke `All Groups`); data E2E-034 tidak menaruh aktor di halaman >1 atau dengan baris tercentang.
- unit `§4.1c#b4` (parsial; kurang; langkah 214, 215, 216, 217): Filter Purchase status 'tersedia bagi aktor Edit Purchase': tidak ada asersi aktor tanpa hak Edit Purchase tidak melihat field `Purchase Status` (E2E-026..033 tidak memeriksanya).
- unit `§4.1c#b4` (parsial; kurang; langkah 214, 215, 216, 217): Aset `No access` bagi pemanggil tidak pernah cocok dan tidak dihitung sehingga `Pending` tidak bocor: tidak ada aktor tanpa hak Purchase (ASTL-LOGIC-10) yang memfilter Purchase Status `Pending` dan memastikan aset di luar hak tidak muncul.
- unit `§4.1c#b4` (parsial; kurang): Server menegakkan aturan di atas pada setiap kueri: tidak ada spec be-e2e (BE-091/BE-090) yang mengasersi filter Purchase status oleh pemanggil tanpa hak.
- unit `ASTL-LOGIC-10j` (parsial; kurang; langkah 16, 21): Klausa 'keadaan tidak berlaku berlaku tanpa memandang hak': tidak ada aktor tanpa hak Asset Class (mis. Group Manager) yang melihat `—` (bukan `No access`) pada aset yang Asset Name-nya tanpa Asset Class. E2E-012 hanya memakai Total Control; E2E-026..033 tidak memeriksa sel Asset Class baris `Kursi Kerja` (tanpa Asset Class).
- unit `ASTL-LOGIC-17a` (parsial; kurang; langkah 11, 15, 17, 27): Yang diasersi hanya Changelog hilang (langkah 17). Tidak diasersi: Activity Log aset ikut terhapus dan riwayat transaksi yang melekat, termasuk record Missing selesai di tab History Missing, ikut terhapus permanen (PRD: 'seluruh lognya (Changelog Asset, Activity Log aset, dan riwayat transaksi ... termasuk record Missing selesai di tab History Missing)'). Tambahkan aset Disposed dengan record Missing selesai dan verifikasi tab History Missing tidak lagi memuatnya.
- unit `ASTL-LOGIC-17a` (parsial; kurang; langkah 42, 43, 44, 45, 46, 47): Tidak diasersi: 'bila pengeluaran baris dari salah satu record gagal, seluruh penghapusan dibatalkan (toast T-25)'; atomisitas (data aset tetap utuh bila salah satu record multi-aset gagal diproses) tidak diuji di spec mana pun.
- unit `ASTL-LOGIC-17m` (parsial; kurang; langkah 37, 39, 42, 44, 46, 48, 51, 53, 56, 58, 61, 63): Urutan prioritas pada Row Action sudah menutup pasangan S-16>S-19, S-16>S-18, S-18>S-19, S-19>S-34, S-34>lock, S-19>lock. Belum teruji: prioritas pada Bulk lintas aset (S-32 paling didahulukan atas S-16/S-18/S-19/S-34) dan S-29 vs S-30 pada seleksi yang memuat dua jenis lock.
- unit `§4.1i#b4` (parsial; kurang; langkah 80, 81, 82, 83, 101, 102, 103): Syarat Complete diasersi positif (langkah 14, BE-088 langkah 5-6), tetapi cabang negatif tidak bisa gagal: langkah 83 dan 103 hanya memeriksa Asset Value Pending, yang juga berlaku karena Purchase Cost kosong (S-23), bukan membuktikan status Purchase tetap Pending. Verifikasi status Purchase lewat filter Purchase Status Pending/Complete untuk: hanya Date terisi, hanya Cost terisi, custom field Purchasing wajib kosong tetap Pending, dan status dihitung ulang tiap simpan (Date dikosongkan kembali ke Pending).
- unit `EC-22` (parsial; kurang; langkah 32): Bagian ui-e2e 'keadaan Disabled dari data nyata' tidak terpenuhi: trace EC-22 menunjuk langkah 32, yang hanya memeriksa item Delete Asset Data dan Manage Disabled dalam menu Bulk Action yang terbuka (aksi lain tersedia). Tidak ada langkah ui-e2e dengan data nyata (aktor tanpa aksi Bulk yang berhak pada aset terpilih, mis. Manage purchase dengan seleksi aset Disposed) yang mengasersi tombol Bulk Action Disabled; UI-061 langkah 91-95 (ui-client) sudah menutup tooltip S-15.
- unit `ASTL-LOGIC-10p` (parsial; kurang; langkah 3, 9): Hanya dua keadaan lisensi FA-7 diuji (aktif dan dicabut). Keadaan Grace Period (kolom custom field Accounting tersedia read-only) tidak diasersi di spec mana pun; 'server tidak mengembalikan nilainya' saat FA-7 tidak aktif juga tidak diasersi (hanya ketersediaan kolom di Setup Column).
- unit `§4.8#r6` (parsial; kurang; langkah 26, 27, 28): Bulk `Manage` Hidden untuk Asset Admin (dan Manage purchase di E2E-031 langkah 26-27) tidak diasersi; Bar Bulk tampil pada kedua aktor itu.
- unit `§8#r3` (parsial; kurang; langkah 14, 111): fields[]: Label, License, Purchase Date, Purchase Cost, Reference Price, Warranty, Additional costs, Document No. sudah diasersi, tetapi entri Changelog untuk perubahan custom field Purchasing (dan field seksi Pembelian lain seperti Provider) tidak diasersi; E2E-038 langkah 25 hanya Purchase Cost.
- unit `§8#b3` (parsial; kurang; langkah 27): System Log untuk 'kegagalan teknis Bulk Label' tidak diasersi; hanya Manage dan Switch Manage. Tambah keadaan Add/Remove Label gagal teknis dan asersi entri System Log.
- unit `ASTL-LOGIC-16e` (parsial; kurang; langkah 11, 12): Hanya pengembalian Borrow pada aset Unmanaged yang diasersi. 'verifikasi, atau penyelesaian Assignment termasuk Unassign' pada aset Unmanaged tidak diasersi; E2E-040 memakai aset managed. Tambah aset Unmanaged ber-Custody Assigned yang di-Unassign dari modul Assignment dan verifikasi badge kembali Available + overlay Unmanaged.
- unit `ASTL-LOGIC-16c` (parsial; kurang; langkah 19, 25): Cabang 'atau didisposal' tidak diasersi: langkah 19 justru mengasersi TAG Paired tetap terpasang pada aset Disposed (DU-046-2) sampai dihapus, tanpa aksi disposal atas aset Unmanaged ber-TAG.
- unit `§9.9#r11` (parsial; kurang; langkah 65, 68): Batas menurut Data Type hanya diuji untuk Text (120). Text Area <= 360, Numeric/Currency <= 15 digit, Percentage 0-100, Phone 4-15 digit tidak diuji.
- unit `§4.1i#b2` (parsial; kurang; langkah 53, 73): Tidak diasersi: jumlah Reference Price >= 0 (input minus/negatif diblok atau ditolak), tidak dikonversi kurs, dan tidak masuk Asset Value, Acquisition Cost, maupun penyusutan (setelah simpan berhasil). Klausa non-dampak butuh asersi ui-e2e pada aset yang tersimpan.
- unit `V-13` (parsial; kurang; langkah 37, 38, 39, 40): Klausa `setelah trim` hanya diuji untuk Document No. (UI-071 langkah 75-79). Provider (UI-073) dan nama Additional cost (UI-074) tidak diuji dengan nilai 120 karakter yang diapit spasi tepi (harus diterima tanpa `Max. 120 characters`).
- unit `EB-FRM-2@edit-purchase` (parsial; kurang): Klausa (e) 'muat ulang atau pindah menu dengan form kotor mengikuti §24.1d dan §24.1e' tidak diasersi di spec mana pun: konfirmasi bawaan browser saat reload dengan form kotor, dan guard navigasi internal (klik sidebar/Back) yang memunculkan dialog Unsaved Changes (`[Cancel]` tetap di form, `[Leave]` melanjutkan). E2E-021 langkah 54 muat ulang hanya sesudah Save sukses.
- unit `ASTL-LOGIC-15q` (parsial; kurang; langkah 11): 'Perubahan nilai License Timing tidak berlaku surut pada proses yang sedang berjalan, hanya pada submit berikutnya' tidak diuji di spec mana pun: tidak ada langkah yang mengubah Managed Action Retry Delay/Managed Transition Time saat jeda atau proses berjalan lalu mengasersi proses itu tidak berubah dan submit berikutnya memakai nilai baru.

## Spec yang tetap draft (0)

Asersi yang masih salah atau tidak bisa dijalankan sesudah perbaikan penutup.

- Tidak ada.

## Catatan tingkat plan (97)

- unit `FLD-02` (ok): Klik tautan Name membuka Asset Detail ('Buka Asset Detail', PRD baris Name) diasersi E2E-010 yang tidak tercatat sebagai penanggung FLD-02.
- unit `FLD-06` (ok): Placeholder `All brands` diasersi UI-058 (ui-client) yang tidak tercatat sebagai penanggung FLD-06.
- unit `FLD-22` (parsial): Nilai sel (garansi terdekat yang belum lewat / tanggal terakhir), hover, filter 'salah satu garansi', dan sort diasersi E2E-013 yang tidak tercatat sebagai penanggung FLD-22.
- unit `§4.2.1#p1` (ok): Grid kartu (satu baris di layar lebar, tiga kolom menengah, dua kolom sempit) diasersi UI-054 yang tidak tercatat sebagai penanggung §4.2.1#p1.
- unit `§4.2.1#p1` (ok): Maksimal 3 kolom pinned diasersi UI-059 yang tidak tercatat sebagai penanggung §4.2.1#p1.
- unit `KartuAll` (ok): Tooltip kartu All `Active assets only. Disposed assets are in the Disposed card.` diasersi UI-063 (ui-client), tetapi UI-063 tidak tercatat sebagai penanggung KartuAll; catat sebagai pemilik/pendukung.
- unit `KartuInTransaction` (ok): Nilai Custody `In Transfer Process` pada kartu In Transaction diasersi E2E-041 yang tidak tercatat sebagai penanggung KartuInTransaction.
- unit `KartuInTransaction` (ok): Rincian hover In Transaction dan aturan jumlah rincian diasersi UI-063 yang tidak tercatat sebagai penanggung KartuInTransaction.
- unit `KartuIssues` (ok): Rincian hover kartu Issues diasersi UI-063 yang tidak tercatat sebagai penanggung KartuIssues.
- unit `KartuIssues` (ok): Tagging `TAG Reported` pada kartu Issues diasersi E2E-046 (dan Missing di E2E-043, Reported Disposal di E2E-044) yang tidak tercatat sebagai penanggung.
- unit `§4.1a#r3` (ok): E2E-039/040/041/044 mengasersi angka kartu In Transaction (Borrowed, Assigned, In Transfer Process, In Disposal Process) tetapi tidak tercatat sebagai penanggung unit ini.
- unit `§4.1a#r4` (ok): E2E-042/043/044/046 mengasersi angka kartu Issues (Damaged, Missing, Reported Disposal, Not Paired Yet, TAG Reported) tetapi tidak tercatat sebagai penanggung unit ini.
- unit `ASTL-LOGIC-14n` (parsial): Cabang 14f ada di E2E-034, spec ini tidak tercatat sebagai penanggung 14n.
- unit `F-ASTL-13` (ok): Read-only sidebar (tanpa Create/Edit/Delete) diasersi di UI-064 langkah 6, bukan di E2E-003; UI-064 tidak tercatat sebagai penanggung F-ASTL-13.
- unit `EB-SRC-1` (ok): Langkah 6 mengasersi teks UI `No results found` pada spec be-e2e (tanpa teks UI); teks itu seharusnya hanya di E2E-004 (langkah 20, 22). Di BE-091 cukup: hasil kosong.
- unit `§5#r4` (ok): Klausa `No access` selalu di akhir (ASTL-LOGIC-10) diasersi di BE-090 langkah 12 dan 14, tidak tercatat sebagai penanggung 5#r4.
- unit `§5#r8` (ok): Rujukan terhapus dibuang diam-diam diasersi UI-059 yang tidak tercatat sebagai penanggung §5#r8.
- unit `§9.6#r7` (ok): 'Tidak dicatat' (Download tidak masuk Activity Log, Changelog, System Log) diasersi E2E-038 yang tidak tercatat sebagai penanggung §9.6#r7.
- unit `§9.6#r7` (ok): `T-05` (toast gagal `Error, failed to download All-Assets.`) diasersi UI-065 yang tidak tercatat sebagai penanggung §9.6#r7.
- unit `EC-25` (ok): Klausa EC-25 selain Asset Value/S-22/S-23 diasersi spec lain yang tidak tercatat: Pending terurut sebelum No access (BE-090), tidak cocok search/filter (E2E-004, E2E-006), Download kosong (E2E-009), dilengkapi lewat D-13 (E2E-021), predikat tidak terbaca dan Disposed berjurnal Posted (E2E-052). Catat sebagai penanggung.
- unit `ASTL-LOGIC-11l` (ok): Klausa Download tidak terpengaruh penanda garansi diasersi di BE-092 langkah 10 (seluruh garansi satu sel tanpa warna), yang tidak tercatat sebagai penanggung unit ini.
- unit `ASTL-LOGIC-15o` (ok): Sumber Switch (aset yang di-Manage berstatus Pending Activation) diasersi E2E-037 (changelog) dan BE-084, tetapi unit hanya mencatat E2E-018 yang menguji sumber Available quota. Catat penanggung tambahan.
- unit `ASTL-LOGIC-15aa` (ok): Penolakan server 422 atas pasangan Switch yang tidak sesuai (beda group, bukan managed, jumlah tidak sama) diasersi BE-084 langkah 26-32, spec itu tidak tercatat sebagai penanggung unit.
- unit `EB-BLK-3` (ok): Satu entri log per item pada Bulk Delete diasersi E2E-038 langkah 42-50 (satu entri User Action per aset); spec itu tidak tercatat sebagai penanggung unit.
- unit `§9.7#r14` (ok): Efek turunan Delete diasersi spec lain yang tidak tercatat: TAG masuk To Be Returned alasan Deleted (E2E-046 langkah 23-24), file terlampir dan record multi-aset (BE-087 langkah 4, 43-47), entri User Action (E2E-038 langkah 35-40).
- unit `EB-FRM-5@edit-purchase` (ok): Pesan 'Warranty name already exists' dan 'Additional cost name already exists' juga diasersi UI-073 langkah 17 dan UI-074 langkah 17; spec itu tidak tercatat sebagai penanggung unit.
- unit `§4.1h#b14` (ok): 'Tanpa entri Activity Log' untuk Print Label diasersi E2E-038 langkah 58-62, bukan E2E-023 (hanya Changelog, langkah 14); catat E2E-038 sebagai penanggung klausa Activity Log.
- unit `§9.2#p9` (ok): Penolakan server Print Label atas aset di luar cakupan, Disposed, dan Unmanaged diasersi BE-081 langkah 49-53, spec itu tidak tercatat sebagai penanggung unit.
- unit `AddtoTransferDraft` (ok): Langkah 51 mengasersi Bulk Add to Transfer Draft Disabled (S-32) untuk aset Borrowed; spec tidak tercatat sebagai penanggung unit.
- unit `AddtoTransferDraft` (ok): Visibilitas Add to Transfer Draft (baris dan Bulk) per level Feature Suite None/Basic/Full diasersi di sini, tetapi spec tidak tercatat sebagai penanggung unit.
- unit `AddtoTransferDraft` (ok): Aktor Asset Admin jenis Transfer (tampil) dan jenis lain (Hidden) diasersi di sini; spec tidak tercatat sebagai penanggung unit. Aktor Group Manager di E2E-027 langkah 10 dan 26 juga tidak tercatat.
- unit `F-ASTL-16.k1` (ok): Penolakan server atas aset non-Unmanaged (BE-084 langkah 20-21) dan lintas group (BE-084 langkah 22-23), serta Manage Disabled lintas group di UI (E2E-018 langkah 10-12, UI-061 langkah 60-66) diasersi spec yang tidak tercatat sebagai penanggung unit; E2E-024 langkah 45-47 menumpuk dua penyebab (lintas group dan Pending Activation) sehingga tidak mengisolasi aturan lintas group.
- unit `F-ASTL-17.k2` (ok): Aset tidak memenuhi syarat membatalkan seluruh aksi diasersi dengan benar di BE-087 (langkah 13-14, 40-41) dan UI-061 (langkah 42-53), tetapi spec itu tidak tercatat sebagai penanggung unit.
- unit `Manage` (ok): Klausa Manage (dialog D-03/D-04 menurut Available, jeda S-14, lintas group S-33, server cakupan, QUOTA_EXCEEDED, Changelog/Activity Log/System Log) diasersi E2E-018, UI-061, UI-068/069, BE-081, BE-084, E2E-038; hanya E2E-024 yang tercatat sebagai penanggung unit.
- unit `MarkasReturned` (ok): Aktor Group Manager untuk Mark as Returned diasersi di E2E-027 (juga 025, 032 langkah 101/110/122/131 untuk Asset Admin Borrow vs jenis lain, 026/028-031 Hidden), tetapi hanya E2E-024 tercatat sebagai penanggung unit.
- unit `MarkasReturned` (ok): Visibilitas Mark as Returned per level Feature Suite (None/Basic/Full) diasersi di sini; spec tidak tercatat sebagai penanggung unit.
- unit `MarkasUnassigned` (ok): Aktor Group Manager untuk Mark as Unassigned diasersi di E2E-027 (juga 025, 032 langkah 126/136 untuk Asset Admin Assignment, 026/028-031 Hidden), tetapi hanya E2E-024 tercatat sebagai penanggung unit.
- unit `MarkasUnassigned` (ok): Visibilitas Mark as Unassigned per level Feature Suite diasersi di sini; spec tidak tercatat sebagai penanggung unit.
- unit `PrintLabel` (ok): Dialog Print Label berisi aset terpilih (Row Action dan Bulk) diasersi di E2E-023 (langkah 20-30); spec itu tidak tercatat sebagai penanggung unit.
- unit `ReportDisposal` (ok): Tooltip S-35 Report Disposal Disabled menurut Custody diasersi di UI-061, dan aktor Report Disposal di spec gating 025-032; keduanya tidak tercatat sebagai penanggung unit.
- unit `ReportMissing` (ok): UI-061 mengasersi Report Missing Disabled + tooltip S-27 pada aset In Transit dan aktif pada aset Borrowed; trace EC-45/S-27 ada, tetapi spec tidak tercatat sebagai penanggung unit. Aktor Group Manager dan Manage asset & TAG (Update) ada di E2E-027 langkah 12 dan E2E-028 langkah 12, juga tidak tercatat.
- unit `Transfer` (ok): Langkah 51 mengasersi Bulk Transfer Disabled (S-32) untuk aset Borrowed; spec tidak tercatat sebagai penanggung unit.
- unit `Transfer` (ok): Visibilitas Transfer per level Feature Suite diasersi di sini; spec tidak tercatat sebagai penanggung unit.
- unit `Transfer` (ok): Aktor Asset Admin jenis Transfer diasersi di sini; E2E-027 (Group Manager) juga; keduanya tidak tercatat sebagai penanggung unit.
- unit `ASTL-LOGIC-10d` (ok): Nilai sel custom field Purchasing bagi pemegang Manage purchase dan No access bagi pihak lain diasersi BE-090 langkah 31-35; spec itu tidak tercatat sebagai penanggung unit (E2E-031 hanya menyatakan ketersediaan kolom, langkah 32).
- unit `§2#r7` (ok): Cakupan 'Group yang dikelola dan descendant' untuk Group Manager hanya terasersi di BE-080 (Dewi, anak IT/GA); E2E-027 tidak punya group descendant. BE-080 tidak tercatat sebagai penanggung unit.
- unit `§4.8#r2` (ok): Kolom 'Role lain' (Hidden) dicakup oleh E2E-033 (menu All Assets Hidden sehingga aksi tidak terjangkau); spec ini tidak tercatat sebagai penanggung unit r2.
- unit `§4.8#r5` (ok): Bulk Batch Replace TAG pada Total Control diasersi E2E-024 yang tidak tercatat sebagai penanggung.
- unit `§4.8#r6` (parsial): Bulk Manage Total Control diasersi E2E-018, tidak tercatat sebagai penanggung.
- unit `§4.8#r7` (ok): Bulk Delete Asset Data Total Control diasersi E2E-020, tidak tercatat sebagai penanggung.
- unit `§9.11#r1` (ok): Cakupan group + descendant untuk Group Manager dan Asset Admin diasersi BE-080, descendant View asset value dan Manage purchase di E2E-029/031; BE-080 tidak tercatat sebagai penanggung.
- unit `ASTL-LOGIC-10k` (ok): Spec 027 mengasersi `No access` (Asset Class, Tax Depreciation Class) tetapi tidak tercatat sebagai penanggung 10k.
- unit `ASTL-LOGIC-10k` (ok): Spec 030 mengasersi `No access` (Purchase Date/Cost/Warranty) tetapi tidak tercatat sebagai penanggung 10k.
- unit `ASTL-LOGIC-10l` (ok): Spec 030 langkah 35 mengasersi `No access`, bukan `Pending`, tetapi tidak tercatat sebagai penanggung 10l.
- unit `EB-AKS-5@add-label` (ok): Add Label sukses oleh pemegang Update saja (Sari) dan ditolak untuk pemegang Delete saja ada di BE-081; spec 028 memakai Update + Delete. BE-081 tidak tercatat sebagai penanggung.
- unit `EB-AKS-5@delete-asset-data` (ok): Delete Asset Data sukses oleh pemegang Read + Delete saja (Tono) ada di BE-081; 028 langkah 79-88 memakai Update + Delete. BE-081 tidak tercatat.
- unit `EB-AKS-5@manage-asset` (ok): BE-081 mengasersi sukses Add/Remove Label dan Manage oleh Read + Update serta Delete oleh Read + Delete, tetapi tidak tercatat sebagai penanggung unit ini.
- unit `EB-AKS-5@remove-label` (ok): Remove Label sukses oleh pemegang Update saja ada di BE-081; 028 memakai Update + Delete. BE-081 tidak tercatat.
- unit `EB-AKS-5@edit-purchase` (ok): BE-081 juga mengasersi Edit Purchase oleh pemegang Manage purchase (Update); tidak tercatat.
- unit `EB-AKS-7` (ok): BE-093 dan E2E-035 memuat satu langkah per aksi tulis modul termasuk Switch Manage (E2E-035 langkah 72, BE-093 langkah 32); BE-093 tidak tercatat sebagai penanggung bagian Switch.
- unit `ASTL-LOGIC-15x` (ok): Entri `Unmanaged` ke `Pending Activation` untuk Manage sumber Available quota diasersi di E2E-018 (037 hanya sumber Switch); tidak tercatat.
- unit `§8#b2` (ok): Entri License di Activity Log dan System Log aktor diasersi di 038 (langkah 23, 27); 038 tidak tercatat sebagai penanggung §8#b2.
- unit `§8#r6` (ok): BE-086 mengasersi Activity Log + tanpa System Log untuk jalur gagal, tidak tercatat sebagai penanggung.
- unit `ASTL-LOGIC-02d` (ok): Klausa TAG pada ASTL-LOGIC-02d diasersi tanpa reload di 046 tetapi unit tidak dicatat sebagai miliknya.
- unit `ASTL-LOGIC-02d` (ok): Klausa audit pada ASTL-LOGIC-02d diasersi tanpa reload di 047 tetapi unit tidak dicatat sebagai miliknya.
- unit `ASTL-LOGIC-17l` (ok): Klausa Hidden pada Row Action dan Bulk Disabled S-32 diasersi E2E-024; alert inline S-32 di UI-070 langkah 89 dan penolakan server di BE-087: tidak tercatat sebagai penanggung.
- unit `ASTL-LOGIC-16h` (ok): Penawaran Report Disposal pada aset Pending Activation (menu hanya Detail, Report Disposal, Delete Asset Data) diasersi di 024 tetapi 024 tidak tercatat sebagai penanggung ASTL-LOGIC-16h.
- unit `§9.7#r12` (ok): Switch Manage (Available tidak berubah) diasersi BE-084; entri License aset yang ditukar di E2E-037 langkah 58/85: tidak tercatat sebagai penanggung.
- unit `§4.1a#p1` (ok): Gating tombol `Print Label` toolbar (hanya pemegang Update) diasersi E2E-025/026/028, bukan UI-054 (Total Control): tidak tercatat sebagai penanggung.
- unit `S-47` (ok): Klausa 'aksi dan Bulk Action Disabled (S-15), Matriks Aksi' diasersi di TC-FA-ASTL-UI-061-menu-aksi-tooltip (step 95, S-15) dan E2E-024 (matriks), bukan di UI-060 yang tercatat pemilik. Tambahkan UI-061/E2E-024 sebagai penanggung S-47.
- unit `§4.4#b3` (ok): Pada UI-060 step 7-8 data hanya 3 baris satu halaman sehingga 'halaman aktif' tidak terbedakan dari 'seluruh hasil'; pembedaan (10 baris halaman aktif dari 12) diasersi di TC-FA-ASTL-E2E-015 step 4-5. Catat E2E-015 sebagai penanggung.
- unit `S-14` (ok): Tooltip S-14 pada Row Action Manage diasersi di E2E-051, bukan di spec yang tercatat sebagai penanggung unit; catat E2E-051 sebagai penanggung S-14 (varian baris).
- unit `S-29` (ok): Tooltip S-29 pada aksi Edit diasersi juga di TC-FA-ASTL-E2E-047-audit-tercermin-dep-audit langkah 9 dan E2E-024 langkah 26/89, tidak tercatat sebagai penanggung S-29.
- unit `§6#r9` (ok): 069 tidak tercatat sebagai penanggung §6#r9 padahal Switch Manage termasuk aksi tulis di unit ini.
- unit `ASTL-LOGIC-15k` (ok): Cakupan 'aset managed pada group yang sama' diasersi TC-FA-ASTL-E2E-019-switch-manage-aset langkah 6-7, spec itu tidak tercatat sebagai penanggung unit ini.
- unit `D-13` (ok): Klausa Bulk (`N assets selected`, tanpa Additional costs, label `Purchase Cost (per asset)` + helper text), penutupan lewat `✕`/`Esc`, dan proteksi form dirty diasersi TC-FA-ASTL-UI-075-dialog-edit-purchase-bulk dan TC-FA-ASTL-UI-076-dialog-edit-purchase-interaksi; keduanya tidak tercatat sebagai penanggung unit ini.
- unit `§4.1i#p1` (ok): Pintu Row Action/Bulk (TC-FA-ASTL-E2E-021, E2E-022) dan aktor Manage purchase/Group Manager (E2E-031, E2E-027) diasersi spec lain yang tidak tercatat sebagai penanggung unit ini.
- unit `FLD-28` (ok): Label Bulk `Purchase Cost (per asset)` dan helper Bulk diasersi UI-075/UI-071, yang tidak tercatat sebagai penanggung FLD-28.
- unit `FLD-29` (ok): Tooltip info `S-37` pada label Reference Price diasersi UI-071 step 11-12 yang tidak tercatat sebagai penanggung FLD-29.
- unit `§4.1i#b2` (parsial): Klausa non-dampak ke Asset Value/Acquisition Cost/penyusutan tidak teramati di ui-client; perlu pemilik ui-e2e (mis. E2E-021) atau pembagian bagian per layer.
- unit `V-13` (parsial): UI-071 mengasersi sisi Document No. unit ini tetapi tidak tercatat sebagai penanggung (hanya UI-073 dan BE-088).
- unit `FLD-34` (ok): Tooltip info `S-36` pada bagian Additional costs diasersi UI-071 step 9-10 yang tidak tercatat sebagai penanggung FLD-34.
- unit `EC-29` (ok): Penolakan 422 Bulk yang memuat Additional costs diasersi BE-088 step 36-37 yang tidak tercatat sebagai penanggung EC-29.
- unit `FI-06` (ok): Penolakan server Bulk dengan Additional costs diasersi BE-088 step 36-37 (be-e2e) yang tidak tercatat sebagai penanggung FI-06.
- unit `FI-10` (ok): Cabang 'nama sama sudah ada -> Warranty until dan Provider diperbarui' diasersi benar di BE-088 (langkah 22-23), bukan di UI-075 (pemilik di plan, ui-client hanya mengasersi isi permintaan, langkah 30). Catat BE-088 sebagai penanggung unit ini.
- unit `§4.1i#b7` (ok): Klausa 'Bulk dengan Additional costs ditolak 422', 'nama sama diperbarui', dan 'satu transaksi: berhasil semua atau tidak sama sekali' diasersi di BE-088 (langkah 17-18, 22-23, 37), bukan di UI-075; catat BE-088 sebagai penanggung unit.
- unit `EB-FRM-2@edit-purchase` (parsial): Klausa (e) keluar dari komponen sehingga tidak bisa di ui-client; tempatkan di spec ui-e2e Edit Purchase satu aset (E2E-021) dan catat sebagai penanggung.
- unit `T-28` (ok): Cabang 'permintaan langsung tanpa perubahan' diasersi di BE-088 (langkah 3 dan 72 sebagai Edit No-Op), bukan di UI-076; catat BE-088 sebagai penanggung unit.
- unit `§4.1h#p4` (ok): UI-069 mengasersi sisi D-04 unit ini (kolom awal Name/Asset ID/Group/Category, Panel Filter memuat Group, Category, Brand, Model / Type, Status, Labels) tetapi tidak tercatat sebagai penanggung (hanya UI-077).
- unit `D-16` (ok): Pintu Row Action dan Bulk Action ke D-16 (tanpa Select Asset) diasersi di E2E-023, bukan di UI-078; catat E2E-023 sebagai penanggung unit.
- unit `ASTL-LOGIC-20o` (ok): E2E-020 langkah 33-34 mengasersi akibat UI aset terhapus (toast T-06, tabel dimuat ulang, D-14 tidak tampil) tetapi tidak tercatat sebagai penanggung unit ini (hanya BE-081).
- unit `F-ASTL-10.k2` (ok): Sisi UI 'aksi tidak ditawarkan bila ada aset Disposed' (ASTL-LOGIC-04a) diasersi di spec UI (mis. UI-061, UI-063) yang tidak tercatat sebagai penanggung unit; BE-083 hanya menegakkan server (PRD butir 8 'DILARANG memproses mutasi label pada aset Disposed').
- unit `F-ASTL-11.k2` (ok): Sama dengan F-ASTL-10.k2: sisi UI 'tidak ditawarkan' dimiliki spec UI yang tidak tercatat; BE-083 langkah 18-19 hanya sisi server.
- unit `V-11` (ok): Alert inline '[Asset] would exceed 10 warranties.' untuk beberapa aset penyebab (daftar gulir) diasersi benar di UI-075, tetapi UI-075 tidak tercatat sebagai penanggung V-11; catat di plan.
- unit `§9.2#p8` (ok): Klausa 'memvalidasi aktor dan cakupan group (Matriks Aksi)' untuk Edit Purchase diasersi di BE-081 (bukan di BE-088); BE-081 tidak tercatat sebagai penanggung unit ini.
- unit `§9.6#r4` (ok): Presedensi 409 atas 422 untuk Edit Purchase diasersi BE-089 langkah 39-43, toast T-20 di E2E-021/022 dan UI-076, tetapi spec-spec itu tidak tercatat sebagai penanggung unit ini.
- unit `ASTL-LOGIC-01d` (ok): Klausa 'UI tidak dinonaktifkan' dan toast baku pada UI diasersi di E2E-035 (ui-e2e), yang tidak tercatat sebagai penanggung unit ini.

