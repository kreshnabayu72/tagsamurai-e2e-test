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

Sumber: generate spec `specs/GlobalSettings/Division/` (76 spec, 296 TC aktif dari `TC-GS-DIV-1` sampai `TC-GS-DIV-296`). Tanggal generate: 2026-10-07.

## GAP-DIV-E2E-007 — Restrukturisasi Dekomposisi Terisolasi (64 → 76 Specs) untuk Ketahanan Runner Otomasi

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-07)  
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
