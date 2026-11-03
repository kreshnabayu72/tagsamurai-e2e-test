---
name: Fixed Asset Settings User
id: suite-fixed-asset-settings-user
description: Spec e2e turunan tc-settings-user.md untuk Fixed Asset > Settings > User
executionOrder: 6.0
parallel: false
---

# Suite: Fixed Asset Settings User

Suite ini mencakup halaman Fixed Asset > Settings > User: User List (Search, Filter, Sort, Pagination, Setup Column, Download, Sidebar Group Tree), Detail User, Activate dan Deactivate (single dan bulk), Resend Activation dan Confirmation Email, Tab Role (Global Role, Group Role, Transaction Role beserta Auto-Revert tier dan Group Manager), Edit Home Group (single dan bulk), Tab Responsibilities (Borrowed Assets, Assigned Assets, Pending Approvals, Pending Tasks), Tab Non-Login User, Tab Changelog, Modal Changelog per sub-tab Role, Modal Combined Changelog, Tab System Log, Tab Transaction Admin Log, Tab User Log, Role Matrix dan scope aktor, pencatatan di tiga surface log, sinkronisasi lintas modul, defense-in-depth, state tenant (Client Suspended dan Expired), ketahanan terhadap kegagalan server, serta tampilan Android.

`parallel: false` karena spec mengubah state yang dipakai bersama: populasi 25 pengguna Client `FaUserMain` yang tampil di User List, penugasan peran dan Home Group Pre-setup, status aktif pengguna, status Client dan plan (Principal Automation), Selection Limit, jam server dan jam browser, serta flag Guided Tooltip. Spec yang menghapus atau mencabut data bersama (App Access, penghapusan identitas, Delete Group, Bulk Deactivate seluruh baris) dan spec kelas h (Suspended, Expired, unsuspend) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, Lina Marlina, Pre-setup #1, `Spectra.env.FA_TC_PASSWORD`) dan menyetel flag Guided Tooltip User List menjadi `seen` untuk akun aktor yang dipakai suite, supaya walkthrough otomatis tidak menutupi layar. Mekanisme penyetelan dan nama flag mengikuti `foundation/functions/guided-tooltip.md` dan disediakan tim FE/BE. Spec Guided Tooltip (TC-FA-SU-17, 18, 19) mengatur flag sendiri sesudah hook ini dan menjelaskan mekanismenya di `## Prerequisites`.
- `beforeEach`: membuka halaman Fixed Asset > Settings > User; menutup dialog `Unsaved Changes` dengan mengonfirmasi `beforeunload` sebagai jaring pengaman (bukan pengganti langkah pemulihan spec, S-09).
- `after`: memulihkan flag Guided Tooltip ke nilai awal tiap akun, memulihkan sesi ke akun default suite, dan menjalankan pemulihan state yang dicatat spec.
- Pre-setup bersama (pengguna dan penugasan Client `FaUserMain`) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat seed API oleh spec yang mengubahnya (Given di `before`, pemulihan di `after`), mengikuti Catatan TC (fixture yang diubah disediakan ulang lewat seed API).
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir. Kemampuan ini disediakan tim BE/FE; `## Prerequisites` spec merujuknya dengan satu baris. Aksi Admin B atau Principal Automation yang hanya memicu perubahan state memakai sesi API; sesi UI kedua dipakai hanya bila hasil di sesi itu diasersi (P-2).
- Principal Automation (Pre-setup #12) sebagai pelaku perubahan status Client, plan, System Limits, dan App Access adalah akun atau kemampuan "disediakan tim FE" (S-13).
- Password akun aktor lewat `Spectra.env.FA_<ROLE>_PASSWORD` sesuai bagian 5 konvensi; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Satu akun, satu nama env password `[KEPUTUSAN 2026-11-02]` (spec tidak membuat nama baru): Qori Akbar #4 `FA_MURG_UPD_PASSWORD`; Rina Susanti #5 `FA_MURG_RO_PASSWORD`; Sinta Dewi #6 `FA_MURGR_UPD_PASSWORD`; Teguh Prakoso #7 `FA_MURGR_RO_PASSWORD`; Oscar Pranata #9 `FA_GM_PASSWORD`; Gita Permata #20 `FA_GITA_PASSWORD`; aktor Read Only `FA_RO_PASSWORD`; Default User `FA_DU_PASSWORD`; Total Control `FA_TC_PASSWORD`. Nama lama `FA_MGUR`, `FA_MGURRO`, `FA_MURG`, `FA_MURGRO` (+ `_PASSWORD`) sudah diganti di semua spec; nilai password tidak berubah, jadi tim FE mengubah nama variabel di `executionConfig.environmentVariables` dan `.env`.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya.
- Spec yang menyimpan konfigurasi kolom Setup Column (`[Save]`, termasuk pin dan urutan) memulihkannya di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`; spec yang melakukannya menyebut kemampuan itu di `## Prerequisites`.
