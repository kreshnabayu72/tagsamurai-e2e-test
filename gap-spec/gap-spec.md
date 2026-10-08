# Gap & Temuan Dekomposisi Spec E2E — Pemisahan Uji Kompleksitas Tinggi

Dokumen ini mencatat seluruh temuan arsitektural dan keputusan dekomposisi terkait **pemisahan skenario uji kompleksitas tinggi** (*high-complexity test case separation*) dari spec screening/fungsional dasar menjadi spec otomasi modular yang terisolasi tinggi.

Pemisahan ini dilakukan untuk:
- Mengeliminasi risiko *cramming* (menumpuk banyak concern teknis heterogen ke satu spec).
- Mencegah kegagalan berantai (*flakiness cascading*) di runner TestSpectra / Playwright CI/CD.
- Mengisolasi fixture dan harness berat (seperti QR canvas decoder, multi-tab context, live mail-catcher polling, fault injection HTTP 500, dan atomic rollback hook) hanya pada spec yang membutuhkannya.
- Mempercepat diagnosis akar masalah saat terjadi kegagalan di pipeline otomasi.

> Untuk temuan gap pada level Test Case granular, PRD, dan kesiapan environment/harness umum, lihat [gap-tc.md](./gap-tc.md).

---

# Auth > MFA (Multi-Factor Authentication)

Sumber: generate spec `specs/Auth/Mfa/` (36 spec, 205 TC aktif dari `TC-AUTH-MFA-01` sampai `TC-AUTH-MFA-205`). Tanggal generate: 2026-10-07.

## GAP-MFA-E2E-008 — Pemisahan Uji Kompleksitas Tinggi dari Spec Screening dan Dekomposisi Modular (30 → 36 Specs)

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-07)  
**Tipe:** arsitektur test case & isolasi eksekusi otomasi  
**Dampak:** tinggi terhadap stabilitas otomasi Playwright dan kecepatan diagnosis kegagalan  

Pada draf awal generasi spec E2E (30 spec), ditemukan pola *cramming* atau penggabungan beberapa pengujian teknis tingkat tinggi ke dalam satu spec screening visual atau spec fungsional biasa:
1. **Decoding QR Code Canvas di Spec Screening (`TC-AUTH-MFA-109` di Spec 004):** Pengujian inspeksi visual Step 1-3 form enrollment digabung dengan decoding gambar/canvas QR code untuk memvalidasi URI `otpauth://totp/` dan parameter RFC 6238 (SHA1, 30s period, secret string). Ini memaksa spec screening visual bergantung pada library decoder eksternal (`jsQR`).
2. **Polling Mail-Catcher di Spec Screening OTP (`TC-AUTH-MFA-62` di Spec 002):** Spec screening tata letak kotak SegmentedInput dan navigasi Backspace digabung dengan request polling kotak masuk email mail-catcher, memperlambat eksekusi screening visual.
3. **Mock Hardware Biometrik di Spec Layout Mobile (`TC-AUTH-MFA-54` di Spec 005):** Pengujian tata letak keypad numerik responsif Android dicampur dengan instrumentasi sensor biometrik (fingerprint / face unlock) pada faktor-1.
4. **Verifikasi Admin GS di Skenario User Biasa (`TC-AUTH-MFA-178` di Spec 026):** Skenario penundaan pencatatan log Success ke faktor-2 menuntut login sebagai Total Control Global Settings di tengah-tengah alur device fingerprinting user browser biasa.
5. **Mega-Specs Heterogen (Spec 028, 029, 030):** Menggabungkan race condition multi-tab/device, flood IP rate limit 429, fault injection 5xx, screen reader ARIA Live, direct API tampering, fallback lost-device, dan paritas tier langganan ke dalam spec yang terlalu padat (16–18 TC per file).

**Dampak Buruk Jika Tidak Dipecah:**
- **Flakiness tinggi:** Kegagalan library decoding QR atau polling email akan menggagalkan seluruh assertion layout screening tombol/input, menyamarkan apakah bug ada pada CSS/DOM atau pada backend format.
- **Fixture berlebih:** Mengharuskan setiap runner menyiapkan konteks multi-tab, proxy hop, dan mail-catcher bahkan untuk pengetesan form sederhana.
- **Diagnosis sulit:** CI/CD reporting gagal menunjukkan akar penyebab secara presisi.

**Solusi & Keputusan yang Diterapkan di Spec:**  
Dilakukan dekomposisi modular menjadi **36 spec terisolasi**:
- `TC-109` (QR URI decode) dipindahkan ke spec khusus **`TC-AUTH-MFA-E2E-032`** (*Verifikasi Kriptografis Isi QR Code & Secret Key*).
- `TC-62` (cek mail-catcher) dipindahkan dari Spec 002 ke **`TC-AUTH-MFA-E2E-016`** (*Verifikasi OTP Auto-Submit & Paste*).
- `TC-54` (biometric hardware) dipisahkan menjadi spec khusus **`TC-AUTH-MFA-E2E-036`** (*Mobile Biometric Re-Login Trigger*).
- `TC-178` (delayed success logging) dipindahkan dari Spec 026 ke **`TC-AUTH-MFA-E2E-028`** (*Audit Log Status Mutasi*).
- Uji balapan multi-tab/device dikonsolidasikan ke **`TC-AUTH-MFA-E2E-033`** (*Konkurensi & Double-Submit Guards*).
- Uji API token tampering dikonsolidasikan ke **`TC-AUTH-MFA-E2E-034`** (*Defense-in-Depth Token Tampering*).
- Uji flood 429 dan 5xx server fault injection diisolasi di **`TC-AUTH-MFA-E2E-035`** (*Rate Limiting & Resilience*).
- Uji recovery user dan admin reset dipisahkan di **`TC-AUTH-MFA-E2E-030`**, sementara paritas subscription & dialog session management diisolasi di **`TC-AUTH-MFA-E2E-031`**.

---

# Global Settings > Activity Log

Sumber: generate spec `specs/GlobalSettings/ActivityLog/` (57 spec, 227 TC aktif dari `TC-GS-ACTLOG-01` sampai `TC-GS-ACTLOG-227`). Tanggal generate: 2026-10-07.

## GAP-ACTLOG-E2E-007 — Dekomposisi Terstruktur Modular Awal (227 TC Granular → 49 Specs)

**Status:** superseded oleh GAP-ACTLOG-E2E-008  
**Tipe:** arsitektur test case  
**Dampak:** pemetaan dasar awal sebelum audit isolasi kegagalan  

---

## GAP-ACTLOG-E2E-008 — Pemisahan Uji Kompleksitas Tinggi dari Spec Heterogen dan Dekomposisi Terisolasi (49 → 57 Specs)

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-07)  
**Tipe:** arsitektur test case & isolasi eksekusi otomasi  
**Dampak:** tinggi terhadap ketahanan (*resilience*) otomasi Playwright, pencegahan kegagalan berantai (*flakiness cascading*), dan kecepatan diagnosis akar masalah di CI/CD  

Pada draf generasi spec 49 file, teridentifikasi adanya penggabungan beberapa pengujian teknis tingkat tinggi ke dalam 1 spec hanya karena berada di halaman atau seksi yang sama:
1. **Autentikasi Kompleks Tab Session (Spec 015):** Menggabungkan 14 TC yang mencakup Login normal, Logout em-dash `—`, gagal login (Bad Credentials & Account Locked), Client Suspended, alur Reset/Change Password, Admin Concurrent Force-Logout, SSO SAML/OIDC, dan Mobile Session ke dalam 1 file. Menuntut mock IdP SSO, user-agent mobile, dan status lockout di satu tempat.
2. **Download CSV/XLSX vs Network Error 500 (Spec 030):** Menggabungkan inspeksi binary buffer CSV (UTF-8 BOM, headers, format) dan XLSX dengan HTTP 500 fault injection toast error dan audit read-only idempotency lintas dua tab.
3. **SSE Real-Time Reaktivitas vs Cross-Tenant Leakage (Spec 045):** Menggabungkan penambahan baris otomatis SSE lokal dan filter guard dengan pengujian keamanan isolasi soket multi-tenant yang membutuhkan koordinasi dua browser context simultan (Alfa vs Beta).
4. **Master Data GS vs File Manager & System Actor Purge (Spec 046):** Menggabungkan mutasi admin biasa pada 9 modul GS dengan aksi permanen Recycle Bin File Manager dan background system auto-purge yang mencatat aktor khusus `Modified By = "System"`.
5. **Database Transaction Rollback vs Immutability & Out-of-Order (Spec 047):** Menggabungkan fault injection database 500 (zero phantom log) dengan pengujian relational immutability user rename dan stream arrival sequencing.
6. **Direct API 403 vs DOM XSS vs Regex Query (Spec 048):** Menggabungkan uji API authorization token 403 dan parameter tampering dengan browser DOM XSS script injection and parser pencarian regex literal.
7. **Client Suspended vs Retensi 3 Tahun vs Paritas Tier Plan (Spec 049):** Menggabungkan penguncian status tenant dengan seed historical data 3 tahun dan paritas 4 tier langganan.

**Solusi & Keputusan yang Diterapkan di Spec (49 → 57 Specs Terisolasi):**
- Spec 015 dipecah menjadi **3 spec**:
  - `015`: *Core Session (Login, Logout status dash `—`, GS Session, Sel Kosong)* (`TC-41, 45, 51, 52, 53, 226`).
  - `016`: *Security Events (Bad Creds, Account Locked, Client Suspended, Reset/Change Password)* (`TC-42, 43, 44, 46, 47`).
  - `017`: *External & Cross-Module Auth (Force-Logout Concurrent, SSO SAML, Mobile App)* (`TC-48, 49, 50`).
- Spec 030 dipecah menjadi **2 spec**:
  - `032`: *Validasi Format Ekspor CSV & XLSX, UTF-8 BOM, & Idempotency* (`TC-122-125, 128-135`).
  - `033`: *Ketahanan Ekspor: HTTP 500 Fault Injection & Toast Error Feedback* (`TC-138, 139`, `Mode: mock`).
- Spec 045 dipecah menjadi **2 spec**:
  - `048`: *Reaktivitas Real-Time SSE Lokal & Filter Guard di Kedua Tab* (`TC-195, 196, 197`).
  - `049`: *Keamanan Multi-Tenant SSE: Isolasi Streaming dan Pencegahan Kebocoran Lintas-Tenant* (`TC-198`).
- Spec 046 dipecah menjadi **2 spec**:
  - `050`: *Ingestion Mutasi Master Data 9 Modul GS, Hardware, & TAG Registry* (`TC-199-208`).
  - `051`: *Ingestion File Manager Permanently Delete & System Auto-Purge Actor Audit* (`TC-209, 210, 211`).
- Spec 047 dipecah menjadi **2 spec**:
  - `052`: *Atomic Rollback Ingestion: Ketiadaan Log pada Operasi DB Gagal / Zero Phantom Log* (`TC-212`).
  - `053`: *Snapshot Immutability Modified By & Pengurutan Kronologis Out-of-Order* (`TC-213, 214`).
- Spec 048 dipecah menjadi **2 spec**:
  - `054`: *Direct API Endpoint Authorization 403 & Multi-Product Parameter Isolation* (`TC-215, 216, 217`).
  - `055`: *Frontend DOM XSS Sanitization Defense & Regex Literal Query Matching* (`TC-218, 219, 220`).
- Spec 049 dipecah menjadi **2 spec**:
  - `056`: *Akses Riwayat dan Logging saat Status Client Suspended/Expired* (`TC-222, 223`).
  - `057`: *Retensi Data Historis Lintas Tahun & Paritas Fungsional Seluruh Tier Langganan* (`TC-224, 225`).

---

# Global Settings > Division

Sumber: generate spec `specs/GlobalSettings/Division/` (89 spec, 296 TC aktif dari `TC-GS-DIV-1` sampai `TC-GS-DIV-296`). Tanggal generate: 2026-10-07.

## GAP-DIV-E2E-007 — Restrukturisasi Dekomposisi Terisolasi (64 → 76 Specs) untuk Ketahanan Runner Otomasi

**Status:** superseded oleh GAP-DIV-E2E-008  
**Tipe:** arsitektur test case & isolasi kegagalan runner  
**Dampak:** tinggi terhadap reliabilitas eksekusi Playwright dan isolasi pelaporan kegagalan  

Pada telaah awal rancangan dekomposisi 64 file, teridentifikasi adanya penggabungan beberapa pengujian teknis tingkat tinggi ke dalam spec screening atau spec fungsional biasa:
1. **Algoritma Auto-Generate Code (`F-DIV-09`):** Pemecahan token dasar, fallback 6 karakter & `DIV`, serta dedup suffix angka dan pemotongan batas 15 karakter digabung dalam 1 file besar. Kegagalan parser token berisiko menggagalkan verifikasi fallback.
2. **Campuran Fault Injection (HTTP 500 & Timeout) dengan Alur Normal:** Mock kegagalan server pada Create, Delete Single, Bulk Delete, dan Download digabungkan ke dalam alur fungsional, memaksa runner menanggung flakiness network mock pada saat menguji form normal.
3. **Konkurensi & Dual Context:** Pengujian race condition auto-generate code 409 dicampur dengan validasi submit biasa.
4. **Pemisahan Screening Mobile dari CRUD Mobile:** Layout visual card list dipisahkan dari alur mutasi bottom sheet form Android.

**Solusi & Keputusan yang Diterapkan di Spec (64 → 76 Specs Terisolasi):**
- Algoritma auto-generate code dipecah menjadi **3 spec modular**:
  - `016`: *Tokenisasi & Delimiter* (`TC-50` s/d `54`)
  - `017`: *Fallback Karakter Simbolik & Non-Latin* (`TC-55`, `56`, `57`, `63`)
  - `018`: *Dedup Suffix Angka & Truncation 15 Karakter* (`TC-58` s/d `62`)
- Kegagalan server & timeout diisolasi ke spec tersendiri:
  - `023`: *Create Resilience (Server 500 & Timeout)* (`TC-67`, `76`, `77`)
  - `032`: *Edit Resilience (Server 500 & Timeout)* (`TC-106`, `110`, `111`)
  - `037`: *Delete Single Resilience (Server 500)* (`TC-122`, `123`)
  - `044`: *Bulk Delete Resilience (Server 500)* (`TC-139`, `140`)
  - `053`: *Main Table Export Resilience & Setup Column Sync* (`TC-183`, `184`, `186`)
  - `061`: *Changelog Export Resilience* (`TC-221`, `222`, `223`)
- Alur Edit No-Op diisolasi menjadi spec tersendiri:
  - `030`: *Edit No-Op Auto-Close Tanpa Log Baru* (`TC-100`)
- Pengujian race condition kode 409 dipisahkan menjadi:
  - `024`: *Transaksi DB Atomik & Auto-Retry Konflik 409* (`TC-79`, `80`)
- Alur mobile dibagi menjadi:
  - `075`: *Screening Layout Mobile Android, Bottom Sheets, dan Gating* (`TC-281` s/d `284`)
  - `076`: *Eksekusi CRUD Mobile Android via Bottom Sheet* (`TC-285`, `286`)

---

## GAP-DIV-E2E-008 — Pemisahan Uji Kompleksitas Tinggi, Dekomposisi Modular Bertahap, dan Eliminasi Spec Marathon (76 → 89 Specs)

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-07)  
**Tipe:** arsitektur test case, eliminasi kegagalan berantai (*flakiness cascading*), & pengurangan beban langkah (*step-budget optimization*)  
**Dampak:** sangat tinggi terhadap stabilitas otomasi Playwright, pencegahan runner timeout, isolasi fixture/state per domain, dan kecepatan diagnosis kegagalan di CI/CD  

Pada telaah lanjutan draf 76 file spec E2E, teridentifikasi sejumlah spec dengan jumlah langkah pengujian berlebih (mulai dari 34 langkah hingga puncaknya 103 langkah) serta pemadatan skenario (*cramming*) dengan prasyarat heterogen (multi-login persona, multi-fase modal, pencampuran batasan sistem dengan interaksi visual, dan pencampuran alur form konsumen dengan import staging). Dilakukan audit restrukturisasi secara bertahap:

### 1. Dekomposisi Bulk Action Bar & Selection Limit (Spec 038 → 3 Specs)
Spec `038` awal memuat 34 langkah uji yang mencampuradukkan screening visual bar, kalkulasi dinamis counter baris, checkbox header multi-page, dan penegakan batas kuota sistem (`Selection Limit = 5`). Dipecah menjadi:
- **`TC-GS-DIV-E2E-042`**: *Screening Bulk Action Bar & Real-time Counter* (`TC-125`, `126`) [10 steps] — Kemunculan bar saat $\ge 1$ baris checked, urutan elemen tombol/teks/icon close, kalkulasi realtime counter, dan dismiss via `(✕)`.
- **`TC-GS-DIV-E2E-043`**: *Checkbox Header, Status Indeterminate, & Seleksi Lintas Halaman Select All* (`TC-127`, `128`) [14 steps] — Checkbox header memilih 10 baris halaman aktif, toggle unselect, status `[-]` indeterminate, tombol `Select All (32 records)`, persistensi seleksi di halaman 2, dan toggle `Unselect All`.
- **`TC-GS-DIV-E2E-044`**: *Penegakan Batas Kuota Selection Limit & Toast Capping* (`TC-129`, `130`) [10 steps] — Prasyarat khusus `Selection Limit = 5`: penonaktifan checkbox baris ke-6 + tooltip `You've reached the maximum selection of 5 rows.`, serta capping parsial `Select All` ke 5 baris pertama dengan persistent toast error warning.

### 2. Dekomposisi Paket Prioritas 1: Eliminasi Spec Monolitik (>50 Steps & Multi-Aktor)
- **Guided Tooltip Walkthrough (Spec `006`, 52 steps → 2 Specs):**
  - **`TC-GS-DIV-E2E-006`**: *Walkthrough Auto-Launch, 3-Step Content, Navigasi Tombol, Overlay Dismiss, & Replay [?]* (`TC-10`, `11`, `12`, `13`, `14`) [33 steps] — Alur visual tur, first-visit trigger, tombol Next/Back/Done, overlay dismiss, flag `seen`, dan replay tur via tombol `[?]`.
  - **`TC-GS-DIV-E2E-007`**: *Walkthrough Keyboard Controls, Viewport Interruption, & Capability Gating* (`TC-15`, `16`, `17`) [19 steps] — Navigasi keyboard (Esc, Enter, panah), resize/pindah halaman membatalkan flag `seen`, dan pelompataan Step 1 (+ Division) untuk peran tanpa hak akses Create.
- **Role Matrix Visibilitas Tab & Kontrol Akses (Spec `007`, 75 steps, 7 persona → 2 Specs):**
  - **`TC-GS-DIV-E2E-008`**: *Role Matrix: Baseline Access & Read-Only Scoping* (`TC-18`, `19`, `23`, `24`) [42 steps] — Tab tersembunyi bagi aktor tanpa capability, mode baca murni Read-Only (tools aktif, aksi/checkbox tersembunyi), peran Read-Only Access Level, dan Total Control baseline.
  - **`TC-GS-DIV-E2E-009`**: *Role Matrix: Isolasi Hak Tulis Granular (Create-Only, Update-Only, Delete-Only)* (`TC-20`, `21`, `22`) [33 steps] — Isolasi kontrol aksi tulis: Create-Only hanya melihat `[+ Division]`, Update-Only hanya melihat row action `Edit`, Delete-Only hanya melihat row action `Delete`, checkbox baris, dan Bulk Action Bar.
- **Filter Changelog Lanjutan & Logika Disjungsi (Spec `059`, 58 steps → 2 Specs):**
  - **`TC-GS-DIV-E2E-065`**: *Kotak Pencarian Dropdown Filter & Logika Disjungsi OR Multi-Opsi* (`TC-204`, `205`, `292`, `293`) [31 steps] — In-dropdown search box pada Action, Field, Division Name, Modified By, dan evaluasi disjungsi OR saat multi-opsi dipilih.
  - **`TC-GS-DIV-E2E-066`**: *Siklus Hapus Chip via X/Uncheck, Overflow Chip, Loading Skeleton, & Snapshot Master Terhapus* (`TC-231`, `232`, `233`, `294`, `295`) [27 steps] — Hapus chip via icon X di form vs uncheck di dropdown, overflow chip tersembunyi, dropdown loading state, dan retensi snapshot riwayat divisi terhapus.
- **Changelog Setup Column 7 Kolom & Modal Lifecycle (Spec `062`, 103 steps → 4 Specs):**
  - **`TC-GS-DIV-E2E-069`**: *Modal Changelog UI Behavior, Pagination 10/25/50/100, Dismiss X/Backdrop, & Format Tanggal General Settings* (`TC-209`, `210`, `211`, `212`) [18 steps] — Header tanpa sort icon, pagination 10/25/50/100, dismiss via X dan backdrop, serta format tanggal/waktu entitas.
  - **`TC-GS-DIV-E2E-070`**: *Setup Column Fase 1: Overlay 7 Kolom, Toggle Hide/Unhide, & Guard Kolom Terakhir* (`TC-213`, `215`, `220`) [26 steps] — Overlay 7 kolom, toggle sembunyikan/tampilkan per kolom, dan guard disabled checkbox + tooltip saat tersisa 1 kolom.
  - **`TC-GS-DIV-E2E-071`**: *Setup Column Fase 2: Modal Dialog, Drag-and-Drop Reorder 7 Kolom, & Freeze Pinning Kolom* (`TC-214`, `216`, `217`) [43 steps] — Screening modal dialog, DnD reorder 7 kolom ke posisi baru, dan sticky freeze pin saat tabel di-scroll horizontal.
  - **`TC-GS-DIV-E2E-072`**: *Setup Column Fase 3: Reset to Default, Pembatalan Cancel/X, Penyimpanan Browser Storage, & Independensi Tabel Utama* (`TC-218`, `219`, `234`) [14 steps] — Tombol Reset to Default, pembatalan draft perubahan, penyimpanan per user di browser, dan independensi dari preferensi kolom tabel utama.

### 3. Dekomposisi Paket Prioritas 2: Peningkatan Kerapian Modular, Simetri Form, & Isolasi Sub-Sistem
- **Create Modal Clear Field vs Unsaved Changes Guard:**
  - **`TC-GS-DIV-E2E-021`**: *Interaksi Form Create: Pengosongan Input Form via Tombol Clear Field Tanpa Menutup Modal* (`TC-64`) [9 steps] — Menguji `[Clear Field]` murni mengosongkan form tanpa menutup modal dan tanpa dialog peringatan.
  - **`TC-GS-DIV-E2E-022`**: *Proteksi Perubahan Belum Disimpan (D-05): Dialog Unsaved Changes pada Icon [✕] & Esc, Serta Blokir Klik Backdrop* (`TC-68`, `69`, `70`, `71`) [29 steps] — Dialog D-05 saat dirty state pada icon close dan Esc, aksi Cancel vs Leave, form clean tanpa dialog, dan pencegahan dismiss klik backdrop.
- **Edit Modal Validasi Name Format vs Uniqueness & Self-Exclusion:**
  - **`TC-GS-DIV-E2E-029`**: *Validasi Field Name pada Edit: Wajib Diisi, Spasi Saja, Trim Spasi, Batas 120/121 Karakter, dan Blokir Emoji* (`TC-83` s/d `88`) [22 steps] — Format inline error: empty, whitespace-only, auto-trim, batas boundary 120/121 karakter, dan blokir emoji.
  - **`TC-GS-DIV-E2E-030`**: *Validasi Keunikan Name pada Edit: Debounce Duplikat, Re-Cek Submit, Pengecualian Nilai Sendiri (Self-Exclusion), dan Toleransi Case Rename* (`TC-89` s/d `92`) [21 steps] — Debounce 500ms duplikat record lain, race submit atomik, pengetikan ulang nama sendiri tanpa error duplicate (self-exclusion), dan rename beda huruf besar-kecil pada diri sendiri.
- **Tabel Utama Search Toolbar Mechanics vs Scoping & Substring:**
  - **`TC-GS-DIV-E2E-051`**: *Pencarian Tabel Utama: Perilaku Toolbar Search, Ekspansi, Auto-Focus, Icon Clear X, Panah Kembali, dan Eksekusi Enter* (`TC-141`, `142`, `143`) [20 steps] — Ekspansi search bar, kursor auto-focus, tombol clear (✕) teks tanpa reset tabel, panah kembali (←) collapse dan reset langsung, serta eksekusi submit Enter tanpa debounce.
  - **`TC-GS-DIV-E2E-052`**: *Pencarian Tabel Utama: Pencocokan Substring Name & Code, Case-Insensitive, Empty State, dan Scoping Kolom Tersembunyi* (`TC-144` s/d `148`) [21 steps] — Pencocokan partial substring Name & Code, case-insensitivity, empty state no results found, dan pengecualian kolom yang di-hide dari pencarian.
- **Tabel Utama Filter Panel vs Active Chips & Search Coexistence:**
  - **`TC-GS-DIV-E2E-053`**: *Filter Panel Tabel Utama: Screening Panel, Date Range Picker, Kepatuhan Format Tanggal DD/MM/YY, dan Reset Clear Field* (`TC-149` s/d `152`) [18 steps] — Toggle panel filter, date range picker Last Updated format General Settings, dan tombol `[Clear Field]`.
  - **`TC-GS-DIV-E2E-054`**: *Filter Tabel Utama: Chip Filter Aktif, Badge Counter Toolbar, dan Koeksistensi Search-Filter* (`TC-153` s/d `157`) [24 steps] — Kemunculan chip filter aktif, hapus chip lewat (✕), badge counter pada toolbar, irisan AND search + filter, dan independensi pembersihan.
- **User Form Stale Auto-Clear vs Import Parity & Missing Divisions:**
  - **`TC-GS-DIV-E2E-079`**: *Penanganan Form User & Non-Login User pada Divisi yang Dihapus Pihak Lain: Error Field dan Auto-Clear Dropdown* (`TC-254`, `255`) [10 steps] — Form Create User & Non-Login User saat divisi terpilih dihapus admin lain sebelum submit menampilkan error field dan auto-clear tanpa mereset form.
  - **`TC-GS-DIV-E2E-080`**: *Parity Operasional Import Division dan Alur [Create Missing Divisions]: Mutasi, Pencatatan Changelog, Batas Limit, dan Penolakan Duplicate* (`TC-256`, `257`, `289`, `290`) [18 steps] — Parity edit/delete divisi hasil import, penolakan Create Missing Divisions saat Master Data Count Limit tercapai, dan penolakan race duplicate.

### 4. Hasil & Metrik Arsitektural Akhir
- **Total Specs:** **89 spec atomik terisolasi penuh** (`TC-GS-DIV-E2E-001` s/d `TC-GS-DIV-E2E-089`).
- **Cakupan Granular:** **100% (296/296 TC terpetakan tepat satu kali)**.
- **Beban Langkah Uji:** Seluruh spec marathon berhasil dieliminasi; langkah uji terpanjang terpangkas dari **103 steps** menjadi maksimal **45 steps**.
- **Integritas Linting:** `npx spectra lint --strict specs/GlobalSettings/Division` terverifikasi **0 lint errors**.

---

# Auth > Login with Password

Sumber: generate spec `specs/Auth/LoginPassword/` (sebelumnya 23 spec, 161 TC aktif terpetakan; setelah dekomposisi **29 spec**, 161 TC aktif dari `TC-AUTH-LP-01` sampai `TC-AUTH-LP-163`). Tanggal generate: 2026-10-06, diperbarui terhadap PRD/TC 2026-10-07; dekomposisi: 2026-10-08.

## GAP-LP-E2E-009 — Pemisahan Uji Kompleksitas Tinggi dari Spec Heterogen dan Dekomposisi Modular (23 → 29 Specs)

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-08)  
**Tipe:** arsitektur test case & isolasi eksekusi otomasi  
**Dampak:** tinggi terhadap stabilitas otomasi Playwright, pencegahan kegagalan berantai (*flakiness cascading*), dan kecepatan diagnosis kegagalan di CI/CD

Pada rangkaian 23 spec `LoginPassword`, teridentifikasi penggabungan beberapa pengujian teknis tingkat tinggi ke dalam 1 spec hanya karena berada di halaman (screen) yang sama:

1. **Injeksi SQL/XSS di Spec Screening Validasi Email (E2E-001, 69 steps):** Uji keamanan payload `' OR 1=1 --` dan `<script>alert(1)</script>` dicampur dengan screening elemen, urutan Tab, validasi format/blur, plus-addressing, case-insensitive, dan boundary 120/121 karakter — concern keamanan tergabung dengan inspeksi visual.
2. **Bypass Server-side & Outage Penyedia di Spec Gate reCAPTCHA (E2E-003):** Skenario token reCAPTCHA dibuang dari payload (Defense-in-Depth) dan simulasi outage penyedia reCAPTCHA (fault injection 503) dicampur dengan ciri evaluasi gate biasa (submit tanpa token, token expired, urutan evaluasi Password kosong mendahului).
3. **Alur Reset Password Lintas Modul vs Semantik Reset Counter (E2E-009, 49 steps — terpanjang):** Pemulihan via modul Reset Password (token email + modul eksternal) digabung dengan semantik reset counter harian oleh login sukses yang memerlukan time-travel dan 4 user fixture tambahan.
4. **Mega-Spec Konfirmasi Agreement (E2E-011, 41 steps):** Validasi checkbox dan pemulihan dicampur dengan stale document 409 (publikasi versi policy via Admin Console), lifecycle token pre-auth (TTL 10 menit + time-travel), tampering token (intercept), double-click guard, dan reuse token — 6 personae + 2 akun principal + TTL mocking dalam satu file.
5. **Verifikasi Absence Log Digabung dengan Pencatatan Kegagalan (E2E-017):** Asersi "baris log TIDAK muncul" (email kosong, format salah, belum terdaftar, lock aktif, navigasi, policy berubah, rate limit) dicampur dengan asersi pencatatan kegagalan (Status/Note spesifik), dua konsep verifikasi yang berlawanan arah; TC-90 (meninggalkan layar Confirm to Continue) bahkan menetap di spec E2E-011 padahal isinya verifikasi absence log.
6. **Data-gap fixture:** E2E-011 mengarahkan langkah tampering token ke user `wahyuhidayat@qwertysystem.net` (TC-143) yang tidak tercantum pada `## Prerequisites` — diperbaiki saat migrasi ke E2E-027 (lihat `gap-tc.md` GAP-LP-E2E-009).

**Solusi & Keputusan yang Diterapkan di Spec (23 → 28 Specs Terisolasi):**

| Spec hasil | Isi | TC sumber | Dipecah dari |
|---|---|---|---|
| **E2E-024** | Defense-in-Depth injeksi SQL & XSS field Email | 144, 145 | E2E-001 |
| **E2E-025** | Defense-in-Depth & resilience token reCAPTCHA (bypass server-side, outage penyedia) | 100, 139 | E2E-003 |
| **E2E-026** | Pemulihan lock counter oleh login sukses tanpa Reset Password (kosong/tanpa captcha tak dihitung, login sukses reset, password benar → Agreement, pasca tahap 1 jam time-travel) | 66, 67, 68, 152, 163 | E2E-009 |
| **E2E-027** | Lifecycle & idempotensi token persetujuan pre-auth (stale doc 409, expired vs sebelum TTL, tampering, double-click, single-use) | 87, 88, 89, 143, 148, 149 | E2E-011 |
| **E2E-028** | Verifikasi kondisi yang TIDAK dicatat di kedua surface log (termasuk meninggalkan layar Confirm to Continue) | 90, 117, 118, 119, 120, 121, 122, 123 | E2E-011 + E2E-017 |
| **E2E-029** | Batas panjang karakter Email (120 lolos, 121 ditolak tanpa blokir input, format menang atas panjang) | 17, 161 | E2E-001 |

Inspirasi pola isolasi: spec rate limit (E2E-015), resilience log (E2E-018), dan concurrency multi-tab (E2E-020) yang sejak awal sudah terisolasi satu-concern.

**Keputusan yang DITAHAN (dengan alasan):**
- **E2E-014, E2E-016, E2E-019, E2E-021, E2E-023** dibiarkan utuh karena seluruh isinya masih satu concern keluarga (resilience server; kolom/derivasi audit; sinkronisasi status; perilaku mobile; persetujuan lintas modul) walaupun memuat harness berat.
- **TC-140 (E2E-007)** dan **TC-142 (E2E-012)** dipertahankan di spec asalnya: keduanya adalah uji defense-in-depth yang konteksnya bergantung pada state lock tahap 1 jam / handoff MFA yang baru saja dibangun pada langkah sebelumnya; memindahkannya ke spec defense generik akan memaksa setup ulang state berat (lock progression / MFA handoff) dan menaikkan total waktu eksekusi.

**Hasil & Metrik Arsitektural Akhir:**
- **Total Specs:** **29 spec atomik** (`TC-AUTH-LP-E2E-001` s/d `TC-AUTH-LP-E2E-029`).
- **Cakupan Granular:** **161/161 TC terpetakan tepat satu kali** (tidak ada duplikat; TC-21/22 tetap di luar spec atas keputusan review terpisah).
- **Beban Langkah Uji:** Puncak spec marathon turun dari **69 steps (E2E-001)** dan **49 steps (E2E-009)** menjadi maksimal **47 steps**; E2E-001 69 → 47, E2E-003 28 → 19, E2E-009 49 → 18, E2E-011 41 → 15, E2E-017 35 → 20.
- **Integritas Linting:** `npx spectra lint --strict specs/Auth/LoginPassword` terverifikasi **0 lint errors** (29 specs and 1 suites verified).

